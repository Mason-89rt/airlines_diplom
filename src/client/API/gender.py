import requests


def get_gender():
    url = 'http://127.0.0.1:8000/gender_start/gender'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def delete_gender(id_):
    data = {"id": id_}
    url = 'http://127.0.0.1:8000/gender_start/new_gender'
    res = requests.delete(url, json=data)
    post_data = res.json()
    return post_data


def put_gender(id_, name):
    data = {"id": id_, "name": name}
    url = 'http://127.0.0.1:8000/gender_start/gender_update'
    res = requests.put(url, json=data)
    post_data = res.json()
    return post_data
