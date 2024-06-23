import requests


def delete_seat_book_on_id(from_directive, to_directive, date_, time_start, time_end, seat_name, passenger_id):
    data = {
        "from_directive": from_directive,
        "to_directive": to_directive,
        "date_": date_,
        "time_start": time_start,
        "time_end": time_end,
        "seat_name": seat_name,
        "passenger_id": passenger_id
    }

    try:
        print("Sending delete request with data:", data)
        response = requests.delete('http://127.0.0.1:8000/bookings_start/seat_name_delete_id', json=data)
        response.raise_for_status()
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        return response.status_code == 200
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response text: {response.text}")
        return False
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return False


def get_seat_book(from_directive, to_directive, date_, time_start_str, time_end_str, seat_name):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_,
            "time_start": time_start_str, "time_end":
            time_end_str, "seat_name": seat_name}
    response = requests.get('http://127.0.0.1:8000/bookings_start/seat_name_book', json=data)
    post_data = response.json()
    return post_data



#print(get_seat_book('Волгоград','Москва','2024-01-21','00:00','04:15','8f'))

def delete_seat_book(passenger_id, from_directive, date_, time_start_str, time_end_str, seat_name, class_name):
    data = {
        "passenger_id": passenger_id,
        "from_directive": from_directive,
        "date_": date_,
        "time_start": time_start_str,
        "time_end": time_end_str,
        "seat_name": seat_name,
        "class_name": class_name
    }
    try:
        print("Sending delete request with data:", data)
        response = requests.delete('http://127.0.0.1:8000/bookings_start/seat_name_delete', json=data)
        response.raise_for_status()
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        return response.status_code == 200
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response text: {response.text}")
        return False
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return False


def id_all_in_bookings_seat(from_directive, to_directive, date_, time_start_str, time_end_str, seat_name,
                            passenger_id,):
    data = {
        "from_directive": from_directive,
        "to_directive": to_directive,
        "date_": date_,
        "time_start": time_start_str,
        "time_end": time_end_str,
        "seat_name": seat_name,
        "passenger_id": passenger_id
    }
    response = requests.get('http://127.0.0.1:8000/bookings_start/id_ticket_bookings_seat', json=data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


def create_seat_book(id_passenger, from_directive, to_directive, date_, seat_name):
    data = {"id_passenger": id_passenger, "from_directive": from_directive, "to_directive": to_directive,
            "date_": date_, "seat_name": seat_name}
    response = requests.post('http://127.0.0.1:8000/bookings_start/booked_ticket_create', json=data)
    post_data = response.json()
    return post_data


def visible_ticket_book(id_passenger):
    data = {"id": id_passenger}
    response = requests.get('http://127.0.0.1:8000/bookings_start/visible_ticket_book', json=data)
    post_data = response.json()
    return post_data
