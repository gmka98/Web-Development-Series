import datetime

from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import arrow
from sqlalchemy import desc

from pds.auth import authenticate_user, create_access_token, get_current_user
from pds.database import get_session
from pds.students import Student
from pds.evaluations import Evaluation
from pds.course import Course
from pds.model import (
    User,
    Token,
    Student,
    Event,
    EvaluationCreateModel,
    EvaluationModel,
    Course
)

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
    {
        "id": 1,
        "user_id": 1,
        "date": "2022-04-25",
        "active_participation": "yes",
        "behavior": "good",
        "acquisition_of_knowledge": "yes",
        "comments": "Great job!",
    },
    {
        "id": 2,
        "user_id": 1,
        "date": "2022-04-20",
        "active_participation": "yes",
        "behavior": "neutral",
        "acquisition_of_knowledge": "partial",
        "comments": "Need to work on understanding the concepts better",
    },
    {
        "id": 3,
        "user_id": 1,
        "date": "2022-04-15",
        "active_participation": "no",
        "behavior": "problematic",
        "acquisition_of_knowledge": "no",
        "comments": "Not engaged in the course",
    },
]


@router.post(
    "/users/{user_id}/evaluations",
    response_model=EvaluationModel,
    status_code=201,
)
async def create_user_evaluations(
    user_id: int,
    payload: EvaluationCreateModel,
    db: Session = Depends(get_session),
):
    ev = Evaluation(
        user_id=user_id,
        active_participation=payload.active_participation,
        behavior=payload.behavior,
        acquisition_of_knowledge=payload.acquisition_of_knowledge,
        comments=payload.comments,
        date=arrow.utcnow().isoformat(),
    )
    db.add(ev)
    db.commit()

    model = EvaluationModel.from_orm(ev)

    return model



#order_by et limit pour lister la derniere evaluations dans sqlalchemy
@router.get("/users/{user_id}/evaluations")
async def get_user_evaluations(user_id: int, db: Session = Depends(get_session)):
    evaluations = db.query(Evaluation).filter_by(user_id=user_id).order_by(desc(Evaluation.date)).limit(3).all()

    if not evaluations:
        raise HTTPException(status_code=404, detail="Evaluations not found")

    last_evaluation = evaluations[0]
    last_evaluations = evaluations

    return {
        "last_evaluation": last_evaluation,
        "evaluations": last_evaluations,
    }


@router.put("/evaluations/{evaluation_id}")
async def update_evaluation(evaluation_id: int, payload: EvaluationModel , db: Session = Depends(get_session)):
    existing_evaluation = db.query(Evaluation).filter_by(id=evaluation_id).first()
    if not existing_evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")
#payload = instance , EvalutionModel = type 
    existing_evaluation.date = payload.date
    existing_evaluation.active_participation = payload.active_participation
    existing_evaluation.behavior = payload.behavior
    existing_evaluation.acquisition_of_knowledge = payload.acquisition_of_knowledge
    existing_evaluation.comments = payload.comments

    db.commit()
    return existing_evaluation



@router.delete("/evaluations/{evaluation_id}")
async def delete_evaluation(evaluation_id: int, db: Session = Depends(get_session)):
    existing_evaluation = db.query(Evaluation).filter_by(id=evaluation_id).first()
    if not existing_evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")

    db.delete(existing_evaluation)
    db.commit()

    return {"message": "Evaluation deleted successfully"}


   

@router.post("/students/",
             response_model=Student,
             status_code=201,
)


def create_student(
    id: int,
    payload: Student,
    db: Session = Depends(get_session),
):
    
    st = Student(
        id=id,
        user_id=user_id,
        email=payload.email,
        status=payload.status,
    )
    db.add(st)
    db.commit()

    model = Student.from_orm(st)

    return model

@router.get("/students")
def read_students():
    return student


@router.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_session)):
    student = db.query(Student).filter(Student.id == student_id.first())
    if not student:
            raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student, db:Session = Depends(get_session)):
    existing_student = db.query(Student).filter(Student.id == student_id.first())
    if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")
    
    existing_student.email = student.email
    existing_student.status = student.status

    db.commit()
    return existing_student


@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session= Depends(get_session)):
    student = db.query(Student).filter(Student.id == student_id.first())
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}


@router.post("/events/{user_id}", response_model=Event, status_code=201)
def create_event(user_id: int, payload: Event, db: Session = Depends(get_session)):
    evt = Event(
        user_id=user_id,
        title=payload.title,
        start=payload.start,
        end=payload.end,
    )
    db.add(evt)
    db.commit()
    db.refresh(evt)
    return evt

    
@router.get("/events/{user_id}")
def get_events(user_id: int, db: Session = Depends(get_session)):
    events = db.query(Event).filter_by(user_id=user_id).all()
    if not events:
        raise HTTPException(status_code=404, detail="Events not found")
    
    return events



@router.put("/events/{event_id}")
def update_event(event_id: int, event: Event, db: Session=Depends(get_session)):
    existing_event = db.query(Event).filter_by(id=event_id).first()
    if not existing_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    existing_event.title=event.title
    existing_event.start=event.start
    existing_event.end=event.end
    db.commit()
    return event


@router.delete("/events/{event_id}")
def delete_event(event_id: int, db:Session = Depends(get_session)):
    existing_event = db.query(Event).filter_by(id=event_id.first())
    if not existing_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(existing_event)
    db.commit()
    return {"message": "Event deleted successfully"}


@router.post("/courses/", response_model=Course, status_code=201)
def create_course(course: Course, db: Session = Depends(get_session)):

    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int, db: Session = Depends(get_session)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: Course, db: Session = Depends(get_session)):
    existing_course = db.query(Course).filter(Course.id == course_id).first()
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    existing_course.title = course.title
    existing_course.description = course.description
    existing_course.teacher_id = course.teacher_id
    existing_course.student_id = course.student_id

    db.commit()
    return existing_course

@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_session)):
    existing_course = db.query(Course).filter(Course.id == course_id).first()
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db.delete(existing_course)
    db.commit()

    return {"message": "Course deleted successfully"}

@router.post("/courses/{course_id}/send/junior", status_code=201)
def send_course_to_junior_students(course_id: int, db: Session = Depends(get_session)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    junior_students = db.query(Student).filter(Student.status == "junior").all()
    if not junior_students:
        raise HTTPException(status_code=404, detail="No junior students found")

    for student in junior_students:
        student.courses.append(course)

    db.commit()

    return {"message": f"Course {course_id} sent to all junior students"}
