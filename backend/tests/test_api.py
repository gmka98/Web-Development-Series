from pds.users import UserManager


def test_user_can_login(client, session):
    um = UserManager(session=session)
    um.create_user(email="alice@acme.test", password="mypassword")

    res = client.post(
        "/api/login",
        data={"username": "alice@acme.test", "password": "mypassword"},
    )
    assert res.status_code == 200, res.text
