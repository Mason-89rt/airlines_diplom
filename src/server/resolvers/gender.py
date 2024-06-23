from endpoints.models import Gender, GenderNameUpdater, GenderDelete
from db.DBmanager import base_manager


def get_gender():
    res = base_manager.execute("select * from gender", args=())
    gender = []
    for i in res:
        gender.append(Gender(id=i[0], name=i[1]))
    return gender


def put_gender_on_id(gender: GenderNameUpdater):
    res = base_manager.execute("update gender set name=? where id=?", args=(gender.name, gender.id))
    return res


def delete_gender(gender: GenderDelete):
    res = base_manager.execute("delete from gender where id=?", args=(gender.id,))
    return res
