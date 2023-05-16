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
