from resolvers.user_state import get_user_state, update_user_state, insert_user_state
from fastapi import APIRouter
from endpoints.models import UserState, UserStateCreate, UserdeleteID

router = APIRouter()


@router.get('/state')
def get_user_endpoint(endpoint: UserdeleteID):
    return get_user_state(endpoint)


@router.put('/state')
def get_user_endpoint(endpoint: UserState):
    return update_user_state(endpoint)


@router.post('/state')
def get_user_endpoint(endpoint: UserStateCreate):
    return insert_user_state(endpoint)
