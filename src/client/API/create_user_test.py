import requests


def post_user_none(name):
    data = {"name": name}
    response = requests.post('http://127.0.0.1:8000/users_start/post_id_on_name_user_getpass', json=data)
    post_data = response.json()
    return post_data


def post_user_getpass(name):
    data = {"name": name}
    response = requests.post('http://127.0.0.1:8000/user_getpass_start/user_getpass', json=data)
    post_data = response.json()
    return post_data


def user_update_on_getpass_role_id(id_, role_id):
    data = {"id": id_, "role_id": role_id}
    response = requests.put('http://127.0.0.1:8000/users_start/user_update_on_getpass_role_id', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def update_user_getpass(id_, login, password, email):
    data = {"id": id_, "login": login, "password": password, "email": email}
    response = requests.put('http://127.0.0.1:8000/users_start/user_update_on_getpass', json=data)
    post_data = response.json()
    return post_data
