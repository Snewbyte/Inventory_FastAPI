# to run tests run pytest in terminal pytest library will scan project and run all tests one by one

from fastapi.testclient import TestClient
from main_controller import app

client = TestClient(app)  # creates a duplicate to do testing on

#############   200    #############

# product
def test_get_product():
    response = client.get("/product?product_id=1", headers={"Authorization": "abcdefg"})
    assert response.status_code == 200

# products
def test_get_all_products():
    response = client.get("/products", headers={"Authorization": "abcdefg"})
    assert response.status_code == 200
    product_response = response.json()  # make json object to check values
    assert product_response[2]["Name"] == "Tomato"
    assert product_response[2]["Price"] == 3.99
    assert type(product_response[0]["ID"]) == int

# products/price
def test_product_price_range():
    response = client.get("products/price?min_price=0&max_price=999", headers={"Authorization": "abcdefg"})
    test = response.json()
    assert response.status_code == 200
    assert isinstance(test, list)

# products/search
def test_product_search():
    response = client.get("/products/search?product_price=1.99&product_type=Vegetable", headers={"Authorization": "abcdefg"})
    test = response.json()
    assert response.status_code == 200
    assert isinstance(test, list)

def test_product_search_price():
    response = client.get("/products/search?product_price=1.99", headers={"Authorization": "abcdefg"})
    test = response.json()
    assert response.status_code == 200
    assert isinstance(test, list)

def test_product_search_type():
    response = client.get("/products/search?product_type=Vegetable", headers={"Authorization": "abcdefg"})
    test = response.json()
    assert response.status_code == 200
    assert isinstance(test, list)

# products/mod
def test_modify_product():
  response = client.post("/products/mod/", json={"ID": 89,"Name": "Foo Berries","Price": 8.99,"Type": "Fruit"}, headers={"Authorization": "abcdefg"})
  assert response.status_code == 200
  assert response.json() == "Successfully updated product"


#############   400    #############

# product 400
def test_product_400():
    response = client.get("/product?product_id=-1", headers={"Authorization": "abcdefg"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Product ID not found"}

# products/price 400
def test_product_price_400():
    response = client.get("/products/price?min_price=-5&max_price=-3", headers={"Authorization": "abcdefg"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No products found in that range"}

# products/search 400
def test_product_search_400():
    response = client.get("/products/search?product_price=-5&product_type=Nut", headers={"Authorization": "abcdefg"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No products found with that criteria"}

#############   401    #############

def test_invalid_token():
    response = client.get("/product?product_id=1", headers={"Authorization": ""})
    assert response.status_code == 401