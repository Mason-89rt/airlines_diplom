import requests


def get_user_state(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/user_state/state', json=data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


def update_user_state(id_, state):
    data = {"user_id": id_, "state": state}
    response = requests.put('http://127.0.0.1:8000/user_state/state', json=data)
    post_data = response.json()
    return post_data


def insert_user_state(user_id, state):
    data = {"user_id": user_id, "state": state}
    response = requests.post('http://127.0.0.1:8000/user_state/state', json=data)
    post_data = response.json()
    return post_data
