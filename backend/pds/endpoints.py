from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from pds.auth import authenticate_user, create_access_token, get_current_user
from pds.database import get_session
from pds.model import User, Token, Student, Event, Evaluation

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

router = APIRouter(prefix="/api")


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session),
):
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token = create_access_token(user)
    return access_token


@router.get("/me")
def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user


# Protected Route
@router.get("/protected_route")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "This is a protected route!"}


# Assume this list of evaluations is coming from a database or another data source

evaluations = [
   
]

@router.post("/users/{user_id}/evaluations", response_model=list[Evaluation])
async def create_user_evaluations(
    user_id: int,
    payload: EvaluationCreateModel,
    db: Session = Depends(get_session)
)
    
    ev = Evaluation(
        user_id=user_id,
        active_participation=payload.active_participation
    )

    db.add(ev)
    db.commit()

@router.get("/users/{user_id}/evaluations")
async def get_user_evaluations(user_id: int):
    user_evaluations = [eval for eval in evaluations if eval["user_id"] == user_id]
    last_evaluations = sorted(user_evaluations, key=lambda x: x["date"], reverse=True)[
        :3
    ]
    return JSONResponse(content=last_evaluations)


@router.put("/evaluations/{evaluation_id}")
async def update_evaluation(evaluation_id: int, evaluation: Evaluation):
    index = next(
        (
            index
            for index, eval in enumerate(evaluations)
            if eval["id"] == evaluation_id
        ),
        None,
    )
    if index is None:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    evaluations[index].update(evaluation)
    return JSONResponse(content=evaluations[index])


@router.delete("/evaluations/{evaluation_id}")
async def delete_evaluation(evaluation_id: int):
    index = next(
        (
            index
            for index, eval in enumerate(evaluations)
            if eval["id"] == evaluation_id
        ),
        None,
    )
    if index is None:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    deleted_evaluation = evaluations.pop(index)
    return JSONResponse(content=deleted_evaluation)

students = []
@router.post("/students")
def create_student(student: Student):
    student_dict = student.dict()
    student_dict["id"] = len(students) + 1
    students.append(student_dict)
    return student_dict


@router.get("/students")
def read_students():
    return students


@router.get("/students/{student_id}")
def read_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error": "Student not found"}


@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for idx, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            students[idx] = student.dict()
            students[idx]["id"] = student_id
            return students[idx]
    return {"error": "Student not found"}


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for idx, student in enumerate(students):
        if student["id"] == student_id:
            del students[idx]
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}

events = []
@router.post("/events")
def create_event(event: Event):
    events.append(event)
    return event


@router.get("/events")
def get_events():
    return events


@router.put("/events/{event_id}")
def update_event(event_id: int, event: Event):
    events[event_id] = event
    return event


@router.delete("/events/{event_id}")
def delete_event(event_id: int):
    event = events.pop(event_id)
    return event
