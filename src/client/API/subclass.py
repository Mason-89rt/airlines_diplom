import requests


def get_subclass():
    url = 'http://127.0.0.1:8000/subclass_start/subclass'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def get_subclass_price():
    url = 'http://127.0.0.1:8000/subclass_start/subclass_price'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def get_subclass_description():
    url = 'http://127.0.0.1:8000/subclass_start/subclass_description'
    res = requests.get(url)
    post_data = res.json()
    return post_data

def get_subclass():
    url = 'http://127.0.0.1:8000/subclass_start/subclass'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def get_description_business():
    url = 'http://127.0.0.1:8000/subclass_start/description_business'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def get_description_economy():
    url = 'http://127.0.0.1:8000/subclass_start/description_economy'
    res = requests.get(url)
    post_data = res.json()
    return post_data
# print(get_subclass_description())
# print(get_subclass_price())
