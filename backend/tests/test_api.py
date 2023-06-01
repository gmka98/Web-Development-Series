from pds.evaluations import Evaluation
from pds.events import Event
from pds.users import UserManager
from pds.students import Student


def test_user_can_login(client, session):
    um = UserManager(session=session)
    um.create_user(email="alice@acme.test", password="mypassword")

    res = client.post(
        "/api/login",
        data={"username": "alice@acme.test", "password": "mypassword"},
    )
    assert res.status_code == 200, res.text


def test_user_can_get_their_own_info(client, session):
    um = UserManager(session=session)
    user = um.create_user(email="alice@acme.test", password="mypassword")

    client.log_as(user)
    res = client.get("/api/me")
    assert res.status_code == 200, res.text


def test_teacher_can_add_an_evaluation_on_a_user(client, session):
    um = UserManager(session=session)
    teacher = um.create_user(email="teacher@acme.test", password="mypassword")
    student = um.create_user(email="student@acme.test", password="mypassword")

    client.log_as(teacher)

    res = client.post(
        f"/api/users/{student.id}/evaluations/",
        json={
            "active_participation": "yes",
            "behavior": "good",
            "acquisition_of_knowledge": "good",
        },
    )

    assert res.status_code == 201, res.text

    created_evaluation = res.json()

    ev = session.query(Evaluation).get(created_evaluation["id"])
    assert ev.user_id == student.id

def test_teacher_can_add_an_event_on_a_user(client, session):
    um = UserManager(session=session)
    teacher = um.create_user(email="teacher@acme.test", password="mypassword")

    client.log_as(teacher)

    res = client.post(
        f"/api/users/{teacher.id}/events/",
        json={
            "title": "first-day",
            "start": "2023-05-25T19:00:00",
            "end": "2023-05-25T23:00:00",
        },
    ) 

    assert res.status_code == 201, res.text

    created_event = res.json()

    ev = session.query(Event).get(created_event["id"])
    assert ev.user_id == teacher.id



def test_teacher_can_create_a_student_on_a_user(client, session):
    um = UserManager(session=session)
    teacher = um.create_user(email="teacher@acme.test", password="mypassword")
    student = um.create_user(email="student@acme.test", password="mypassword")

    client.log_as(teacher)

    res = client.post(
        f"/api/users/{student.id}/students/",
        json={
            "email": "blabla@acme.test",
            "status": "junior",
        },
    )

    assert res.status_code == 201, res.text

    created_student = res.json()

    st = session.query(Student).get(created_student["id"])
    assert st.user_id == teacher.id


def test_teacher_can_add_a_course_on_a_student(client, session):
    um = UserManager(session=session)
    teacher = um.create_user(email="teacher@acme.test", password="mypassword")
    student = um.create_user(email="student@acme.test", password="mypassword")

    client.log_as(teacher)

    res = client.post(
    f"/api/users/{student.id}/course",
    json={
        "name": "fundamental",
        "level": 0,
        "category": "blabla"
    },
)

#endpoint cree cours 