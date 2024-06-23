import requests


def get_date_user(date_birthday):
    data = {"date_birthday": date_birthday}
    response = requests.get('http://127.0.0.1:8000/passenger_start/passenger', json=data)
    post_data = response.json()
    return post_data


def get_profile_info(a, s, d, f, id_gender, id_):
    data = {"name": a, "surname": s, "date_birthday": d, "phone": f, "id_gender": id_gender, "id_": id_}
    response = requests.get('http://127.0.0.1:8000/passenger_start/passenger_profile', json=data)
    post_data = response.json()
    return post_data


def get_profile(id_):
    data = {"id_": id_}
    response = requests.get('http://127.0.0.1:8000/passenger_start/passenger_profile_text', json=data)
    post_data = response.json()
    return post_data


def post_personal_id(id_):
    data = {"id": id_}
    url = 'http://127.0.0.1:8000/passenger_start/new_id'
    response = requests.post(url, json=data)
    return response


def post_personal_info(data):
    url = 'http://127.0.0.1:8000/passenger_start/new_personal_info'
    response = requests.post(url, json=data)
    post_data = response.json()
    return post_data


def put_personal_info(a, s, d, f, id_gender, id_):
    data = {"name": a, "surname": s, "date_birthday": d, "phone": f, "id_gender": id_gender, "id_": id_}
    url = 'http://127.0.0.1:8000/passenger_start/passenger_profile'
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Данные успешно обновлены.")
        return True
    else:
        print(f"Ошибка при обновлении. Код ошибки: {response.status_code}")
        return False


def post_contact(phone):
    data = {"phone": phone}
    response = requests.post('http://127.0.0.1:8000/passenger_start/new_contact', json=data)
    if response.status_code == 200:
        print("Данные успешно отправлены.")
        return True
    else:
        print(f"Ошибка при отправке данных. Код ошибки: {response.status_code}")
        return False


def delete_passenger(id_):
    data = {"id": id_}
    response = requests.delete('http://127.0.0.1:8000/passenger_start/passenger/id', json=data)
    return response

