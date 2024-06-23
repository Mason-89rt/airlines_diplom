import requests


def post_user_getpass(name):
    data = {"name": name}
    response = requests.post('http://127.0.0.1:8000/user_getpass_start/user_getpass', json=data)
    post_data = response.json()
    return post_data


def get_user_getpass_name(name):
    data = {"name": name}
    response = requests.get('http://127.0.0.1:8000/user_getpass_start/user_getpass_name', json=data)
    post_data = response.json()
    if post_data:
        return post_data[0][0]
    else:
        return None

# print(get_user_getpass_name('passenger'))

def get_user_getpass_id(name):
    data = {"name": name}
    response = requests.get('http://127.0.0.1:8000/user_getpass_start/user_getpass_id', json=data)
    post_data = response.json()
    if post_data:
        return post_data[0][0]
    else:
        return None
