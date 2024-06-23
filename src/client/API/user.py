import requests


def get_login_user(login):
    data = {"login": login}
    response = requests.get('http://127.0.0.1:8000/users_start/users_login', json=data)
    post_data = response.json()
    return post_data


def get_id_all():
    data = {}
    response = requests.get('http://127.0.0.1:8000/users_start/all_id', json=data)
    post_data = response.json()
    return post_data


def get_login_password_email_user(login, password, email):
    data = {"login": login, "password": password, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/login_password_email', json=data)
    post_data = response.json()
    return post_data


def get_login_password_user(login, password):
    data = {"login": login, "password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/user/login_password', json=data)
    post_data = response.json()
    return post_data


def get_login_email_user(login, email):
    data = {"login": login, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/login_email', json=data)
    post_data = response.json()
    return post_data


def get_password_email_user(password, email):
    data = {"password": password, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/password_email', json=data)
    post_data = response.json()
    return post_data




def get_id_login_user(id_, login):
    data = {"id": id_, "login": login}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_login', json=data)
    post_data = response.json()
    return post_data


def get_id_password_user(id_, password):
    data = {"id": id_, "password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_password', json=data)
    post_data = response.json()
    return post_data


def get_id_email_user(id_, email):
    data = {"id": id_, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_email', json=data)
    post_data = response.json()
    return post_data


def get_id_login_password_user(id_, login, password):
    data = {"id": id_, "login": login, "password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_login_password', json=data)
    post_data = response.json()
    return post_data


def get_id_login_email_user(id_, login, email):
    data = {"id": id_, "login": login, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_login_email', json=data)
    post_data = response.json()
    return post_data


def get_id_password_email_user(id_, password, email):
    data = {"id": id_, "password": password, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_password_email', json=data)
    post_data = response.json()
    return post_data


def get_id_login_password_email_user(id_, login, password, email):
    data = {"id": id_, "login": login, "password": password, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user/id_login_password_email', json=data)
    post_data = response.json()
    return post_data


def get_id_user(login):
    data = {"login": login}
    response = requests.get('http://127.0.0.1:8000/users_start/users/select_id', json=data)
    post_data = response.json()
    return post_data[0]


def get_role_id(email):
    data = {"email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/users/select_role_id', json=data)
    post_data = response.json()
    return post_data[0]


def get_email(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/users_start/email', json=data)
    post_data = response.json()
    if post_data:
        return post_data[0]
    else:
        return None


def get_email_user(email):
    data = {"email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/user_email', json=data)
    post_data = response.json()
    return post_data


def get_password_user(password):
    data = {"password": password}
    response = requests.get('http://127.0.0.1:8000/users_start/user_password', json=data)
    post_data = response.json()
    return post_data


def get_role_id_user(role_id):
    data = {"role_id": role_id}
    response = requests.get('http://127.0.0.1:8000/users_start/user_role_id', json=data)
    post_data = response.json()
    return post_data


def get_user_on_id(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/users_start/users/id', json=data)
    post_data = response.json()
    return post_data


def get_all_user():
    response = requests.get('http://127.0.0.1:8000/users_start/users')
    post_data = response.json()
    return post_data


def check_user(login, password, email):
    data = {"login": login, "password": password, "email": email}
    response = requests.get('http://127.0.0.1:8000/users_start/users/check', json=data)
    post_data = response.json()
    return post_data


def update_user_getpass(id_, login, password, email):
    data = {"id": id_, "login": login, "password": password, "email": email}
    response = requests.put('http://127.0.0.1:8000/users_start/user_update_on_getpass', json=data)
    post_data = response.json()
    return post_data


def user_update_on_getpass_role_id(id_, role_id):
    data = {"id": id_, "role_id": role_id}
    response = requests.put('http://127.0.0.1:8000/users_start/user_update_on_getpass_role_id', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def post_user_none(name):
    data = {"name": name}
    response = requests.post('http://127.0.0.1:8000/users_start/post_id_on_name_user_getpass', json=data)
    post_data = response.json()
    return post_data


def update_user(id_, login, password, email, role_id):
    data = {"id": id_, "login": login, "password": password, "email": email, "role_id": role_id}
    response = requests.put(f'http://127.0.0.1:8000/users_start/user_update', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def update_user_role(id_, role_id):
    data = {"id": id_, "role_id": role_id}
    response = requests.put(f'http://127.0.0.1:8000/users_start/user_update_role', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def update_user_login(id_, login):
    data = {"id": id_, "login": login}
    response = requests.put(f'http://127.0.0.1:8000/users_start/user_update_login', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def update_user_password(id_, password):
    data = {"id": id_, "password": password}
    response = requests.put(f'http://127.0.0.1:8000/users_start/user_update_password', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def update_user_email(id_, email):
    data = {"id": id_, "email": email}
    response = requests.put(f'http://127.0.0.1:8000/users_start/user_update_email', json=data)
    if response.status_code != 200:
        print(f"Ошибка при обновлении пользователя: {response.text}")
    return response


def delete_user(id_):
    data = {'id': id_}
    response = requests.delete(f'http://127.0.0.1:8000/users_start/user', json=data)
    if response.status_code != 200:
        print(f"Ошибка при удалении пользователя: {response.text}")
    return response
