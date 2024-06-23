from fastapi import APIRouter
from endpoints.models import UserGetpass, UserGetpassCreate
from resolvers.user_getpass import create_user_getpass, get_user_getpass_name, get_user_getpass_id
router = APIRouter()


@router.post('/user_getpass')
def get_user_endpoint(endpoint: UserGetpassCreate):
    return create_user_getpass(endpoint)


@router.get('/user_getpass_name')
def get_user_endpoint(endpoint: UserGetpass):
    return get_user_getpass_name(endpoint)


@router.get('/user_getpass_id')
def get_user_endpoint(endpoint: UserGetpass):
    return get_user_getpass_id(endpoint)
