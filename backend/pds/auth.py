from passlib.context import CryptContext
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from jose import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .model import User, Token
from . import database 
from sqlalchemy.orm import Session

import os

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
acces_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

print(secret_key)
print(algorithm)
print(acces_token_expire_minutes)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here, you can decode the JWT token, extract user information,
    # and perform any necessary validation or database lookups.
    # This is just a placeholder implementation, and you should customize it to your needs.
    decoded_token = jwt.decode(token, "your-secret-key", algorithms=["HS256"])
    user_id = decoded_token.get("sub")
    db = get_db()
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(user: User) -> Token:
    expires_delta = timedelta(minutes=acces_token_expire_minutes)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"sub": user.email, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return Token(access_token=encoded_jwt)

def authenticate_user(email: str, password: str, db: Session) -> User:
    user = db.query(User).filter(User.email == email).first()
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

