import requests


def get_seat(id_):
    data = {"id": id_}
    response = requests.get('http://127.0.0.1:8000/seat_start/seat_name', json=data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


def get_seat_name_for_economy(economy):
    data = {"economy": economy}
    response = requests.get('http://127.0.0.1:8000/seat_start/seat_name_for_economy', data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


print(get_seat_name_for_economy('Эконом'))


def get_seat_name_for_business(business):
    data = {"business": business}
    response = requests.get('http://127.0.0.1:8000/seat_start/seat_name_for_business', data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


print(get_seat_name_for_business('Бизнес'))
