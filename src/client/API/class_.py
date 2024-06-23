import requests


def get_class():
    url = 'http://127.0.0.1:8000/class_start/class'
    res = requests.get(url)
    post_data = res.json()
    return post_data
