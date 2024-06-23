import requests


def get_salary():
    url = 'http://127.0.0.1:8000/salary_start/salary'
    res = requests.get(url)
    post_data = res.json()
    return post_data


def post_salary(amount):
    data = {"amount": amount}
    url = 'http://127.0.0.1:8000/salary_start/new_salary'
    res = requests.post(url, json=data)
    post_data = res.json()
    return post_data


def put_salary(id_, amount):
    data = {"id": id_, "amount": amount}
    url = 'http://127.0.0.1:8000/salary_start/salary_update'
    res = requests.put(url, json=data)
    post_data = res.json()
    return post_data


def delete_salary(id_):
    data = {"id": id_}
    url = 'http://127.0.0.1:8000/salary_start/salary_delete'
    res = requests.delete(url, json=data)
    post_data = res.json()
    return post_data
