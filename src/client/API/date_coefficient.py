import requests


def get_date_coefficient():
    response = requests.get('http://127.0.0.1:8000/date_coefficient_start/date_coefficient')
    post_data = response.json()
    return post_data


def get_date_coefficient_():
    response = requests.get('http://127.0.0.1:8000/date_coefficient_start/date_coefficient_without_id')
    post_data = response.json()
    return post_data


def get_date_(date_):
    data = {"date_": date_}
    response = requests.get('http://127.0.0.1:8000/date_coefficient_start/date_', json=data)
    post_data = response.json()
    return post_data


def update_date_coefficient(id_, coefficient):
    data = {"id": id_, "coefficient": coefficient}
    response = requests.put('http://127.0.0.1:8000/date_coefficient_start/date_coefficient_update', json=data)
    post_data = response.json()
    return post_data
