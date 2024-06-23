import requests


def get_staff():
    response = requests.get('http://127.0.0.1:8000/staff_start/staffs')
    post_data = response.json()
    return post_data


def get_staff_info(a, s, f, d, id_gender, id_):
    data = {"name": a, "surname": s, "phone": f, "date_birthday": d, "id_gender": id_gender, "id": id_}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff_info', json=data)
    post_data = response.json()
    return post_data


def update_staff_info(a, s, f, d, id_gender, id_):
    data = {"name": a, "surname": s, "phone": f, "date_birthday": d, "id_gender": id_gender, "id": id_}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff_info_update', json=data)
    post_data = response.json()
    return post_data


def get_staff_profile(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff_profile', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_id(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/id', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_phone(phone):
    data = {"phone": phone}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/phone', json=data)
    post_data = response.json()
    return post_data


def get_phone(phone):
    data = {"phone": phone}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff_phone', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_name(name):
    data = {"name": name}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/name', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_surname(surname):
    data = {"surname": surname}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/surname', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_id_gender(id_):
    data = {"gender": id_}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/id_gender', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_id_salary(id_):
    data = {"salary": id_}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/id_salary', json=data)
    post_data = response.json()
    return post_data


def get_staff_on_name_surname(name, surname):
    data = {"name": name, "surname": surname}
    response = requests.get('http://127.0.0.1:8000/staff_start/staff/name_surname', json=data)
    post_data = response.json()
    return post_data


def put_staff_name(id_, name):
    data = {"id": id_, "name": name}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff/name', json=data)
    post_data = response.json()
    return post_data


def put_staff_surname(id_, surname):
    data = {"id": id_, "surname": surname}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff/surname', json=data)
    post_data = response.json()
    return post_data


def put_staff_phone(id_, phone):
    data = {"id": id_, "phone": phone}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff/phone', json=data)
    post_data = response.json()
    return post_data


def put_staff_id_gender(id_, id_gender):
    data = {"id": id_, "id_gender": id_gender}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff/id_gender', json=data)
    post_data = response.json()
    return post_data


def put_staff_id_salary(id_, id_salary):
    data = {"id": id_, "id_salary": id_salary}
    response = requests.put('http://127.0.0.1:8000/staff_start/staff/id_salary', json=data)
    post_data = response.json()
    return post_data


def post_personal_staff_id(id_):
    data = {"id": id_}
    url = 'http://127.0.0.1:8000/staff_start/staff/new_id'
    response = requests.post(url, json=data)
    return response


def post_staff(name, surname, phone, id_gender, id_salary):
    data = {"name": name, "surname": surname, "phone": phone, "id_gender": id_gender, "id_salary": id_salary}
    url = 'http://127.0.0.1:8000/staff_start/new_staff'
    response = requests.post(url, json=data)
    return response


def delete_staff_id(id_):
    data = {"id": id_}
    response = requests.delete('http://127.0.0.1:8000/staff_start/staff/id', json=data)
    post_data = response.json()
    return post_data
