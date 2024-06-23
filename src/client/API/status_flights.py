import requests


def get_status(id_):
    data = {"id_": id_}
    url = 'http://127.0.0.1:8000/start_status_flights/status'
    res = requests.get(url, json=data)
    post_data = res.json()
    if post_data:
        return post_data
    else:
        return None
