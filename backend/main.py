from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

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

