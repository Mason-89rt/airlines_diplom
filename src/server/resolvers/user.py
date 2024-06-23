from endpoints.models import (User, UserID, UserLogin, UserEmail, User_check, UserdeleteID, UserRole,
                              UserPassword, UserLoginID, UserEmailID, UserPasswordID, UserRoleID, UserIDLoginEmail,
                              UserIDPasswordEmail, UserIDLoginPasswordEmail, UserIDLoginPassword, UserLoginPassword,
                              UserPasswordEmail, UserLoginEmail, UserLoginPasswordEmail, UserGetpass, UserUpdate)
from db.DBmanager import base_manager


def get_user():
    res = base_manager.execute("select * from user", args=(), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_id():
    res = base_manager.execute("select id from user", args=(), many=True)
    return res


def get_email(user: UserdeleteID):
    res = base_manager.execute("select email from user where id=?", args=(user.id,), many=False)
    return res


def get_user_login_password_email(user: UserLoginPasswordEmail):
    res = base_manager.execute("select * from user where login = ? and password = ? and email = ?",
                               args=(user.login, user.password, user.email),
                               many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4]))
    return users


def get_user_login_password(user: UserLoginPassword):
    res = base_manager.execute("select * from user where login = ? and password = ?", args=(user.login, user.password),
                               many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_login_email(user: UserLoginEmail):
    res = base_manager.execute("select * from user where login = ? and email = ?", args=(user.login, user.email),
                               many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_password_email(user: UserPasswordEmail):
    res = base_manager.execute("select * from user where password = ? and email = ?", args=(user.password, user.email),
                               many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_login(user: UserLogin):
    res = base_manager.execute("select * from user where id = ? and login = ?", args=(user.id, user.login), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_password(user: UserPassword):
    res = base_manager.execute("select * from user where id = ? and password = ?", args=(user.id, user.password),
                               many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_email(user: UserEmail):
    res = base_manager.execute("select * from user where id = ? and email = ?", args=(user.id, user.email), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_login_email(user: UserIDLoginEmail):
    res = base_manager.execute("select * from user where id = ? and login = ? and email = ?",
                               args=(user.id, user.login, user.email), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_login_password(user: UserIDLoginPassword):
    res = base_manager.execute("select * from user where id = ? and login = ? and password = ?",
                               args=(user.id, user.login, user.password), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_password_email(user: UserIDPasswordEmail):
    res = base_manager.execute("select * from user where id = ? and password = ? and email = ?",
                               args=(user.id, user.password, user.email), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id_login_password_email(user: UserIDLoginPasswordEmail):
    res = base_manager.execute("select * from user where id = ? and login = ? and password = ? and email = ?",
                               args=(user.id, user.login, user.password, user.email), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_user_id(user: UserdeleteID):
    res = base_manager.execute("select * from user where id=?", args=(user.id,), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_id_user(user: UserLoginID):
    res = base_manager.execute("select id from user where login=?", args=(user.login,), many=False)
    return res


def get_role_id(user: UserEmailID):
    res = base_manager.execute("select role_id from user where email=?", args=(user.email,), many=False)
    return res


def get_password_user(user: UserPasswordID):
    res = base_manager.execute("select * from user where password=?", args=(user.password,), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_role_id_user(user: UserRoleID):
    res = base_manager.execute("select * from user where role_id=?", args=(user.role_id,), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def get_login_user(user: UserLoginID):
    res = base_manager.execute("select * from user where login=?", args=(user.login,), many=True)
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def user_email(user: UserEmailID):
    res = base_manager.execute("select * from user where email=?", args=(user.email,))
    users = []
    for us in res:
        users.append(User(id=us[0], login=us[1], password=us[2], email=us[3], role_id=us[4], id_user_getpass=us[5]))
    return users


def check_user(user: User_check):
    res = base_manager.execute("select login, password, email, role_id from user where login=? and password=? "
                               "and email=?",
                               args=(user.login, user.password, user.email))
    return res


def update_user(user: UserUpdate):
    res = base_manager.execute("update user set login=?,password=?,email=? where id_user_name_system=?",
                               args=(user.login, user.password, user.email, user.id))
    return res


def post_id_user_getpass(user: UserGetpass):
    res = base_manager.execute("insert into user(id_user_name_system) select user_name_system.id from user_name_system where name=?",
                               args=(user.name,))
    return res


def put_user(user: UserID):
    res = base_manager.execute("update user set login=?, password=?, email=?, role_id=? where id=?",
                               args=(user.login, user.password, user.email, user.role_id, user.id_))
    return res


def put_user_role_getpass(user: UserRole):
    res = base_manager.execute("update user set role_id=? where id_user_name_system=?",
                               args=(user.role_id, user.id))
    return res


def put_user_role(user: UserRole):
    res = base_manager.execute("update user set role_id=? where id=?",
                               args=(user.role_id, user.id))
    return res


def put_user_login(user: UserLogin):
    res = base_manager.execute("update user set login=? where id=?",
                               args=(user.login, user.id))
    return res


def put_user_password(user: UserPassword):
    res = base_manager.execute("update user set password=? where id=?",
                               args=(user.password, user.id))
    return res


def put_user_email(user: UserEmail):
    res = base_manager.execute("update user set email=? where id=?",
                               args=(user.email, user.id))
    return res


def delete_user(user: UserdeleteID):
    res = base_manager.execute("delete from user where id=?", args=(user.id,))
    return res
