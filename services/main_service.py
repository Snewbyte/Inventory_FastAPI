from modules.user_module import User


def get_user_by_id_query(user_id):
    return f'SELECT * FROM USER WHERE ID={user_id}'


def get_all_users_query():
    return f'SELECT * FROM USER'


def convert_data_to_module(data):
    converted = []
    # Once data gets here, within for loop every row becomes a tuple
    for value in data:
        # (0, 'Ross', 'Geller', '32', 'USA') <- example data
        converted.append(User(ID=value[0], FirstName=value[1], LastName=value[2], Age=value[3], Country=value[4]))
    return converted

