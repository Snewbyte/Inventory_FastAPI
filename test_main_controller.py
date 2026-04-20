# to run tests run pytest in terminal pytest library will scan project and run all tests one by one

from fastapi.testclient import TestClient
from main_controller import app

client = TestClient(app)  # creates a duplicate to do testing on




#############   200    #############

# product 200
def test_get_product():
    response = client.get('/product?product_id=1')
    assert response.status_code == 200

# products 200
def test_get_all_products():
    response = client.get("/products")
    assert response.status_code == 200
    product_response = response.json()  # make json object to check values
    assert product_response[2]["Name"] == "Tomato"
    assert product_response[2]["Price"] == 3.99
    assert type(product_response[0]["ID"]) == int

# products/price 200
def test_product_price():
    response = client.get("products/price?min_price=0&max_price=999")
    test = response.json()
    assert isinstance(test, list)

# products/search 200
#def test_product_search():


#############   400    #############

# product 400
def test_product_400():
    response = client.get('/product?product_id=999')
    assert response.status_code == 400
# products 400

# products/price 400

# products/search 400





def test_yes_product():
    response = client.get("/product?product_id=3")
    assert response.status_code == 200
    assert response.json()["ID"] == 3