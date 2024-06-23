from endpoints.models import UserGetpass, UserGetpassCreate
from db.DBmanager import base_manager


def create_user_getpass(user_getpass: UserGetpassCreate):
    res = base_manager.execute("insert into user_name_system(name) values(?)", args=(user_getpass.name,), many=True)
    return res


def get_user_getpass_name(user_getpass: UserGetpass):
    res = base_manager.execute("select name from user_name_system where name=?", args=(user_getpass.name,), many=True)
    return res


def get_user_getpass_id(user_getpass: UserGetpass):
    res = base_manager.execute("select id from user_name_system where name=?", args=(user_getpass.name,), many=True)
    return res
