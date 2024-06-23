from fastapi import APIRouter
from endpoints.models import Directive
from resolvers.route import get_route
router = APIRouter()


@router.get('/route')
def get_endpoint(endpoint: Directive):
    return get_route(endpoint)
