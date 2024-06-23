import requests


def get_flights():
    response = requests.get('http://127.0.0.1:8000/flights_start/flights')
    post_data = response.json()
    return post_data


def get_gate_flights(from_directive, to_directive):
    data = {"from_directive": from_directive, "to_directive": to_directive}
    response = requests.get('http://127.0.0.1:8000/flights_start/gate_flights', json=data)
    post_data = response.json()
    return post_data


def get_number_flights(from_directive, to_directive):
    data = {"from_directive": from_directive, "to_directive": to_directive}
    response = requests.get('http://127.0.0.1:8000/flights_start/number_flights', json=data)
    post_data = response.json()
    return post_data


def create_flights(flights_status, from_directive, to_directive, time_start, time_end, date_, plane_model, gate):
    data = {"flights_status": flights_status, "from_directive": from_directive, "to_directive": to_directive,
            "time_start": time_start, "time_end": time_end, "date_": date_, "plane_model": plane_model, "gate": gate}
    response = requests.post('http://127.0.0.1:8000/flights_start/flights_create', json=data)
    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"
    try:
        post_data = response.json()
        return post_data
    except requests.exceptions.JSONDecodeError:
        return f"Error: Unable to decode JSON response: {response.text}"


#print(create_flights('По расписанию','Волгоград','Москва',
#                     '04:15','08:30','2024-01-02','Boeing 737','d9'))


def update_flights(id_, flights_status, from_directive, to_directive, time_start, time_end, date_, plane_model, gate):
    data = {"id_": id_, "flights_status": flights_status, "from_directive": from_directive, "to_directive": to_directive,
            "time_start": time_start, "time_end": time_end, "date_": date_, "plane_model": plane_model, "gate": gate}
    response = requests.put('http://127.0.0.1:8000/flights_start/flights_update', json=data)
    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"
    try:
        post_data = response.json()
        return post_data
    except requests.exceptions.JSONDecodeError:
        return f"Error: Unable to decode JSON response: {response.text}"



# print(update_flights(4, 'По расписанию','Сочи','Стамбул',
#                      '04:15','08:30','2024-09-18','Boeing 737','d8'))
