from pydantic import BaseModel


class Evaluation(BaseModel):
    id: int
    user_id: int


class Event(BaseModel):
    title: str
    start: str
    end: str


class Student(BaseModel):
    id: int
    email: str
    status: str


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    is_admin: bool


class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class EvaluationCreateModel(BaseModel):
    active_participation: str
    behavior: str
    acquisition_of_knowledge: str
    comments: str | None


class EvaluationModel(EvaluationCreateModel):
    id: int
    user_id: int
    date: str

    class Config:
        orm_mode = True
