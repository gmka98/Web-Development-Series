from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from .database import get_session
from .model import Token
from .security import verify_password
from .settings import get_settings
from .users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here, you can decode the JWT token, extract user information,
    # and perform any necessary validation or database lookups.
    # This is just a placeholder implementation, and you should customize it to your needs.
    settings = get_settings()
    decoded_token = jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
    user_id = decoded_token.get("sub")
    db = next(get_session())
    user = db.query(User).filter_by(email=user_id).one
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def create_access_token(user: User) -> Token:
    settings = get_settings()
    expires_delta = timedelta(minutes=settings.acces_token_expire_minutes)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"sub": user.email, "exp": expire}
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
    return Token(
        access_token=encoded_jwt,
        token_type="access_token",
    )


def authenticate_user(email: str, password: str, db: Session) -> User:
    user = db.query(User).filter(User.email == email).one()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
