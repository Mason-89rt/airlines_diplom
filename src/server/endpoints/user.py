from fastapi import APIRouter
from endpoints.models import (UserID, UserLogin, UserEmail, User_check, UserdeleteID, UserRole,
                              UserPassword, UserLoginID, UserEmailID, UserRoleID, UserPasswordID, UserIDLoginEmail,
                              UserIDPasswordEmail, UserIDLoginPasswordEmail, UserIDLoginPassword, UserLoginPassword,
                              UserPasswordEmail, UserLoginEmail, UserLoginPasswordEmail, UserGetpass, UserUpdate)
from resolvers.user import (get_login_user, get_user, get_id_user, get_role_id, update_user, put_user, delete_user,
                            user_email, check_user, put_user_role, put_user_password, put_user_login, put_user_email,
                            get_password_user, get_role_id_user, get_user_id, get_user_id_login, get_user_id_email,
                            get_user_id_password, get_user_id_login_email, get_user_id_password_email,
                            get_user_id_login_password, get_user_id_login_password_email, get_user_login_email,
                            get_user_login_password, get_user_password_email, get_user_login_password_email,
                            get_id, get_email, post_id_user_getpass, put_user_role_getpass)
router = APIRouter()


@router.get('/user/id_login')
def get_user_endpoint(endpoint: UserLogin):
    return get_user_id_login(endpoint)


@router.get('/all_id')
def get_user_endpoint():
    return get_id()


@router.get('/email')
def get_user_endpoint(user: UserdeleteID):
    return get_email(user)


@router.post('/post_id_on_name_user_getpass')
def get_user_endpoint(endpoint: UserGetpass):
    return post_id_user_getpass(endpoint)


@router.put('/user_update_on_getpass_role_id')
def get_user_endpoint(endpoint: UserRole):
    return put_user_role_getpass(endpoint)


@router.get('/user/login_password_email')
def get_user_endpoint(endpoint: UserLoginPasswordEmail):
    return get_user_login_password_email(endpoint)


@router.get('/user/login_password')
def get_user_endpoint(endpoint: UserLoginPassword):
    return get_user_login_password(endpoint)


@router.get('/user/login_email')
def get_user_endpoint(endpoint: UserLoginEmail):
    return get_user_login_email(endpoint)


@router.get('/user/password_email')
def get_user_endpoint(endpoint: UserPasswordEmail):
    return get_user_password_email(endpoint)


@router.get('/user/id_password')
def get_user_endpoint(endpoint: UserPassword):
    return get_user_id_password(endpoint)


@router.get('/user/id_email')
def get_user_endpoint(endpoint: UserEmail):
    return get_user_id_email(endpoint)


@router.get('/user/id_login_password')
def get_user_endpoint(endpoint: UserIDLoginPassword):
    return get_user_id_login_password(endpoint)


@router.get('/user/id_login_email')
def get_user_endpoint(user: UserIDLoginEmail):
    return get_user_id_login_email(user)


@router.get('/user/id_password_email')
def user_login(user: UserIDPasswordEmail):
    return get_user_id_password_email(user)


@router.get('/user/id_login_password_email')
def get_user_email(user: UserIDLoginPasswordEmail):
    return get_user_id_login_password_email(user)


@router.get('/users/select_id')
def get_user_endpoint(endpoint: UserLoginID):
    return get_id_user(endpoint)


@router.get('/users/id')
def get_user_endpoint(endpoint: UserdeleteID):
    return get_user_id(endpoint)


@router.get('/users/select_role_id')
def get_user_endpoint(endpoint: UserEmailID):
    return get_role_id(endpoint)


@router.get('/users/check')
def get_user_endpoint(endpoint: User_check):
    return check_user(endpoint)


@router.get('/users')
def get_user_endpoint():
    return get_user()


@router.get('/users_login')
def user_login(user: UserLoginID):
    return get_login_user(user)


@router.get('/user_email')
def get_user_email(user: UserEmailID):
    return user_email(user)


@router.get('/user_password')
def get_user_email(user: UserPasswordID):
    return get_password_user(user)


@router.get('/user_role_id')
def get_user_email(user: UserRoleID):
    return get_role_id_user(user)


@router.put('/user_update_on_getpass')
def new_user(user: UserUpdate):
    return update_user(user)


@router.put('/user_update')
def put_user_name(user_update: UserID):
    return put_user(user_update)


@router.put('/user_update_role')
def put_user_(user_update: UserRole):
    return put_user_role(user_update)


@router.put('/user_update_login')
def put_user_(user_update: UserLogin):
    return put_user_login(user_update)


@router.put('/user_update_password')
def put_user_(user_update: UserPassword):
    return put_user_password(user_update)


@router.put('/user_update_email')
def put_user_(user_update: UserEmail):
    return put_user_email(user_update)


@router.delete('/user')
def delete_user_id(endpoint: UserdeleteID):
    return delete_user(endpoint)
