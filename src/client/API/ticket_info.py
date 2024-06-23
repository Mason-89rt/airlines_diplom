import requests
from src.server.set import routes_coeff
from datetime import datetime
from API.date_coefficient import get_date_coefficient_

from_direct = 'Москва'
to_direct = 'Волгоград'
date_direct = '2024-01-03'
def get_description_economy():
    response = requests.get('http://127.0.0.1:8000/description_economy_start/description_economy')
    post_data = response.json()
    return post_data


def get_description_business():
    response = requests.get('http://127.0.0.1:8000/description_business_start/description_business')
    post_data = response.json()
    return post_data


def get_ticket_time_flight(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/ticket_start/ticket_time', json=data)
    post_data = response.json()
    return post_data

# print(get_ticket_time_flight(from_direct, to_direct, date_direct))
def calculate_flight_duration(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/ticket_start/ticket_time', json=data)
    post_data = response.json()
    durations = []
    for sublist in post_data:
        start_time_str, end_time_str = sublist
        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")
        if end_time < start_time:
            end_time = end_time.replace(day=end_time.day + 1)
        duration = end_time - start_time
        duration_formatted = "{}ч:{}м".format(duration.seconds // 3600, (duration.seconds % 3600) // 60)
        durations.append(duration_formatted)
    return durations


def get_ticket_time(from_directive, to_directive, date_):
    from _datetime import datetime
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/ticket_start/ticket_time', json=data)
    post_data = response.json()
    time_all = []
    for time_range in post_data:
        start_time, end_time = time_range
        start_hour = datetime.strptime(start_time, "%H:%M").hour
        if 0 <= start_hour < 4:
            time_all.append("night")
        else:
            time_all.append("day")
    return time_all
print(get_ticket_time(from_direct, to_direct, date_direct))

def increase(price, factor):
    return price * factor


def get_price_economy_base_(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/subclass_start/ticket_price_economy_base', json=data)
    post_data = response.json()
    r = (from_directive, to_directive)
    y = date_
    time_ = get_ticket_time(from_directive, to_directive, date_)
    date_coefficient = get_date_coefficient_()
    prices = []
    if (r in routes_coeff) and (y in date_coefficient):
        coefficient = float(date_coefficient[y])
        for time_range in time_:
            if time_range == 'day':
                price = post_data[0][0] * routes_coeff[r] * 0.8 * coefficient
                prices.append(int(price))
            elif time_range == 'night':
                price = post_data[0][0] * routes_coeff[r] * 0.9 * coefficient
                prices.append(int(price))
        return prices
    else:
        print(f"Для маршрута {from_directive}-{to_directive} нет информации о цене или коэффициенте")
        return None


def get_price_business_base_(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/subclass_start/ticket_price_business_base', json=data)
    post_data = response.json()
    r = (from_directive, to_directive)
    y = date_
    time_ = get_ticket_time(from_directive, to_directive, date_)
    date_coefficient = get_date_coefficient_()
    prices = []
    if (r in routes_coeff) and (y in date_coefficient):
        coefficient = float(date_coefficient[y])
        for time_range in time_:
            if time_range == 'day':
                price = post_data[0][0] * routes_coeff[r] * 0.8 * coefficient
                prices.append(int(price))
            elif time_range == 'night':
                price = post_data[0][0] * routes_coeff[r] * 0.9 * coefficient
                prices.append(int(price))
        return prices


def get_price_subclass_business(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/subclass_start/ticket_price_business_base', json=data)
    post_data = response.json()
    r = (from_directive, to_directive)
    y = date_
    time_ = get_ticket_time(from_directive, to_directive, date_)
    date_coefficient = get_date_coefficient_()
    prices_night, pr = [], []
    if (r in routes_coeff) and (y in date_coefficient):
        coefficient = float(date_coefficient[y])
        for time_range in time_:
            if time_range == 'day':
                price = post_data[0][0] * routes_coeff[r] * 0.8 * coefficient
                price_standard = post_data[1][0] * routes_coeff[r] * 0.7 * coefficient
                price_plus = post_data[2][0] * routes_coeff[r] * 0.6 * coefficient
                pr.append([int(price), int(price_standard), int(price_plus)])
            if time_range == 'night':
                price = post_data[0][0] * routes_coeff[r] * 0.9 * coefficient
                price_standard = post_data[1][0] * routes_coeff[r] * 0.8 * coefficient
                price_plus = post_data[2][0] * routes_coeff[r] * 0.7 * coefficient
                prices_night.append([int(price), int(price_standard), int(price_plus)])
        return prices_night, pr
    else:
        print(f"Для маршрута {from_directive}-{to_directive} нет информации о цене или коэффициенте")
        return None


def get_price_subclass_economy(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/subclass_start/ticket_price_economy_base', json=data)
    post_data = response.json()
    r = (from_directive, to_directive)
    y = date_
    time_ = get_ticket_time(from_directive, to_directive, date_)
    date_coefficient = get_date_coefficient_()
    prices_night, pr = [], []
    if (r in routes_coeff) and (y in date_coefficient):
        coefficient = float(date_coefficient[y])
        for time_range in time_:
            if time_range == 'night':
                price = post_data[0][0] * routes_coeff[r] * 0.9 * coefficient
                price_standard = post_data[1][0] * routes_coeff[r] * 0.8 * coefficient
                price_plus = post_data[2][0] * routes_coeff[r] * 0.7 * coefficient
                prices_night.append([int(price), int(price_standard), int(price_plus)])
            if time_range == 'day':
                price = post_data[0][0] * routes_coeff[r] * 0.8 * coefficient
                price_standard = post_data[1][0] * routes_coeff[r] * 0.7 * coefficient
                price_plus = post_data[2][0] * routes_coeff[r] * 0.6 * coefficient
                pr.append([int(price), int(price_standard), int(price_plus)])
        return prices_night, pr
    else:
        print(f"Для маршрута {from_directive}-{to_directive} нет информации о цене или коэффициенте")
        return None


print(get_price_subclass_economy(from_direct, to_direct, date_direct))




def get_id_plane(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/bookings_start/id_plane', json=data)
    post_data = response.json()
    if post_data:
        try:
            return int(post_data[0][0])
        except IndexError:
            return None
    else:
        return None
