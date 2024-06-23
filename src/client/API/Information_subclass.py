import requests


def get_subclass_information():
    url = 'http://127.0.0.1:8000/subclass_information_start/subclass_description'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def put_subclass_information(id_, description):
    data = {"id": id_, "description": description}
    url = 'http://127.0.0.1:8000/subclass_information_start/subclass_description_update'
    res = requests.put(url, json=data)
    post_data = res.json()
    return post_data
