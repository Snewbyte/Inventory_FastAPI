from modules.product_module import Product, ProductRequest, ProductTypeEnum

# keep query in SQL functions, so I know calls pertain to SQL queries

##################### POST #####################

# use single quotes for main return for double quotes inside for valid SQL statements
def insert_new_product_query(new_product : ProductRequest):
    return f'INSERT INTO PRODUCTS(ID, NAME, PRICE, TYPE) VALUES ({new_product.ID}, "{new_product.Name}", "{new_product.Price}", "{new_product.Type}")'

def update_product_query(product_data : ProductRequest):
    return f'UPDATE PRODUCTS SET NAME="{product_data.Name}", PRICE="{product_data.Price}", TYPE="{product_data.Type}" WHERE ID={product_data.ID}'


##################### GET #####################

def get_product_by_id_query(product_id):
    return f'SELECT * FROM PRODUCTS WHERE ID={product_id}'

def get_all_products_query():
    return f'SELECT * FROM PRODUCTS'

def get_products_price_range_query(min_price: float, max_price: float):
    return f'SELECT * FROM PRODUCTS WHERE {min_price} <= PRICE <= {max_price}'

def search_products_query(price: float = None, type: ProductTypeEnum = None):
    if price is not None and type is not None:
        return f'SELECT * FROM PRODUCTS WHERE PRICE = {price} AND TYPE = "{type.value}"'
    elif price is not None:
        return f'SELECT * FROM PRODUCTS WHERE PRICE = {price}'
    elif type is not None:
        return f'SELECT * FROM PRODUCTS WHERE TYPE = "{type.value}"'
    else:
        return f'SELECT * FROM PRODUCTS'  # just return everything if neither is given


### CONVERT ###

def convert_data_to_module(data):
    converted = []
    # Once data gets here, within for loop every row becomes a tuple
    for value in data:
        # (0, 'Apple', 4.99, 'Fruit') <- example data
        converted.append(Product(ID=value[0], Name=value[1], Price=value[2], Type=value[3]))
    return converted

