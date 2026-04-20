# to run tests run pytest in terminal pytest library will scan project and run all tests one by one

from fastapi.testclient import TestClient
from main_controller import app

client = TestClient(app)  # creates a duplicate to do testing on


# even though we're testing multiple conditions each function counts as 1 test
def test_get_all_users():
    response = client.get("/user/all")
    assert response.status_code == 200
    user_response = response.json()  # make json object to check values
    assert user_response[2]["FirstName"] == "Phoebe"
    assert user_response[2]["LastName"] == "Buffay"
    assert type(user_response[0]["ID"]) == int


def test_get_user():
    response = client.get('/user?user_id=999')
    assert response.status_code == 400

    response = client.get("/user?user_id=3")
    assert response.status_code == 200
    assert response.json()["ID"] == 3