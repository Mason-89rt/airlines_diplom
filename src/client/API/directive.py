import requests


def get_directive(from_directive, to_directive):
    data = {"from_directive": from_directive, "to_directive": to_directive}
    response = requests.get('http://127.0.0.1:8000/directive_start/directive', json=data)
    post_data = response.json()
    return post_data


def get_directive_all():
    response = requests.get('http://127.0.0.1:8000/directive_start/directive_all')
    post_data = response.json()
    return post_data


def get_directive_from(from_directive):
    data = {"from_directive": from_directive}
    response = requests.get('http://127.0.0.1:8000/directive_start/directive_from', json=data)
    post_data = response.json()
    return post_data


def get_directive_to(to_directive):
    data = {"to_directive": to_directive}
    response = requests.get('http://127.0.0.1:8000/directive_start/directive_to', json=data)
    post_data = response.json()
    return post_data


def update_directive_from(id_, from_directive):
    data = {"id": id_, "from_directive": from_directive}
    response = requests.put('http://127.0.0.1:8000/directive_start/directive_from', json=data)
    post_data = response.json()
    return post_data


def update_directive_to(id_, to_directive):
    data = {"id": id_, "to_directive": to_directive}
    response = requests.put('http://127.0.0.1:8000/directive_start/directive_to', json=data)
    post_data = response.json()
    return post_data


def create_directive(from_directive, to_directive):
    data = {"from_directive": from_directive, "to_directive": to_directive}
    response = requests.post('http://127.0.0.1:8000/directive_start/new_directive', json=data)
    post_data = response.json()
    return post_data


def delete_directive(id_):
    data = {"id": id_}
    response = requests.delete('http://127.0.0.1:8000/directive_start/directive', json=data)
    post_data = response.json()
    return post_data
