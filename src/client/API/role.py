import requests


def get_role():
    url = 'http://127.0.0.1:8000/role_start/roles'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def post_role(role):
    data = {"name": role}
    url = 'http://127.0.0.1:8000/role_start/new_role'
    res = requests.post(url, json=data)
    post_data = res.json()
    return post_data


def put_role(id_, role):
    data = {"id": id_, "name": role}
    url = 'http://127.0.0.1:8000/role_start/role_update'
    res = requests.put(url, json=data)
    post_data = res.json()
    return post_data


def delete_role(id_):
    data = {"id": id_}
    url = 'http://127.0.0.1:8000/role_start/role_delete'
    res = requests.delete(url, json=data)
    post_data = res.json()
    return post_data
