import requests


def get_seat_buy(from_directive, to_directive, date_, time_start_str, time_end_str, seat_name):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_,
            "time_start": time_start_str, "time_end":
                time_end_str, "seat_name": seat_name}
    response = requests.get('http://127.0.0.1:8000/purchased_ticket_start/seat_name_buy', json=data)
    post_data = response.json()
    return post_data


def create_buy_ticket(id_passenger, from_directive, to_directive, date_, seat_name):
    data = {"id_passenger": id_passenger, "from_directive": from_directive, "to_directive": to_directive,
            "date_": date_, "seat_name": seat_name}
    response = requests.post('http://127.0.0.1:8000/purchased_ticket_start/buy_ticket_create', json=data)
    post_data = response.json()
    return post_data


def visible_buy_ticket_book(id_passenger):
    data = {"id": id_passenger}
    response = requests.get('http://127.0.0.1:8000/purchased_ticket_start/visible_buy_ticket_book', json=data)
    post_data = response.json()
    return post_data
print(visible_buy_ticket_book(3))