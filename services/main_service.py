from modules.user_module import User, UserRequest


### POST ###

# use single quotes for main return for double quotes inside for valid SQL statements
def insert_new_user(new_user : UserRequest):
    return f'INSERT INTO USER(ID, FIRST_NAME, LAST_NAME, AGE, COUNTRY) VALUES ({new_user.ID}, "{new_user.FirstName}", "{new_user.LastName}", "{new_user.Age}", "{new_user.Country}")'

def update_user(user_data : UserRequest):
    return f'UPDATE USER SET FIRST_NAME="{user_data.FirstName}", LAST_NAME="{user_data.LastName}", AGE="{user_data.Age}", COUNTRY="{user_data.Country}" WHERE ID={user_data.ID}'


### GET ###

def get_user_by_id_query(user_id):
    return f'SELECT * FROM USER WHERE ID={user_id}'


def get_all_users_query():
    return f'SELECT * FROM USER'


### CONVERT ###

def convert_data_to_module(data):
    converted = []
    # Once data gets here, within for loop every row becomes a tuple
    for value in data:
        # (0, 'Ross', 'Geller', '32', 'USA') <- example data
        converted.append(User(ID=value[0], FirstName=value[1], LastName=value[2], Age=value[3], Country=value[4]))
    return converted

