from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from backend.auth import authenticate_user, create_access_token, get_user_by_email
from .models import User, Token
from .database import get_db


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

@app.post("/api/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token = create_access_token(user)
    return access_token

@app.get("/api/me")
def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user

# Protected Route
@app.get("/api/protected_route")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "This is a protected route!"}

# Assume this list of evaluations is coming from a database or another data source
evaluations = [
    {
        "id": 1,
        "user_id": 1,
        "date": "2022-04-25",
        "active_participation": "yes",
        "behavior": "good",
        "acquisition_of_knowledge": "yes",
        "comments": "Great job!"
    },
    {
        "id": 2,
        "user_id": 1,
        "date": "2022-04-20",
        "active_participation": "yes",
        "behavior": "neutral",
        "acquisition_of_knowledge": "partial",
        "comments": "Need to work on understanding the concepts better"
    },
    {
        "id": 3,
        "user_id": 1,
        "date": "2022-04-15",
        "active_participation": "no",
        "behavior": "problematic",
        "acquisition_of_knowledge": "no",
        "comments": "Not engaged in the course"
    }
]

@app.get("/users/{user_id}/evaluations")
async def get_user_evaluations(user_id: int):
    user_evaluations = [eval for eval in evaluations if eval["user_id"] == user_id]
    last_evaluations = sorted(user_evaluations, key=lambda x: x["date"], reverse=True)[:3]
    return JSONResponse(content=last_evaluations)

