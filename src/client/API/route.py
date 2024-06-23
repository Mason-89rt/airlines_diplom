import requests


def get_route(from_directive, to_directive, date_):
    data = {"from_directive": from_directive, "to_directive": to_directive, "date_": date_}
    response = requests.get('http://127.0.0.1:8000/route_start/route', json=data)
    post_data = response.json()
    if post_data:
        return post_data
    else:
        return None


def route_exists(from_directive, to_directive):
    data = {"from_directive": from_directive, "to_directive": to_directive}
    response = requests.get('http://127.0.0.1:8000/route_start/route_exists', json=data)
    post_data = response.json()
    if post_data:
        return True
    else:
        return None
