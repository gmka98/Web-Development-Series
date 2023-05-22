from pds.evaluations import Evaluation
from pds.users import UserManager


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
