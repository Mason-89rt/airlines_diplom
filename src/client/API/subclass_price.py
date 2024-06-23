import requests


def get_subclass_price():
    url = 'http://127.0.0.1:8000/subclass_price_start/subclass_price'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def put_subclass_price(id_, price):
    data = {"id": id_, "price": price}
    url = 'http://127.0.0.1:8000/subclass_price_start/subclass_price_update'
    res = requests.put(url, json=data)
    post_data = res.json()
    return post_data
