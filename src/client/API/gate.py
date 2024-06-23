import requests


def get_gate(from_):
    data = {"from_": from_}
    url = 'http://127.0.0.1:8000/gate_start/gate'
    res = requests.get(url, json=data)
    post_data = res.json()
    if post_data:
        return post_data
    else:
        return None
