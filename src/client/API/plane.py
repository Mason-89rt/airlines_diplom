import requests


def get_model_plane(id_):
    data = {"id_": id_}
    url = 'http://127.0.0.1:8000/model_plane_start/model_plane'
    res = requests.get(url, json=data)
    post_data = res.json()
    if post_data:
        return post_data
    else:
        return None
