from fastapi import APIRouter
from endpoints.models import Directive, DirectiveFromTo
from resolvers.route import get_route, route_exist
router = APIRouter()


@router.get('/route')
def get_endpoint(endpoint: Directive):
    return get_route(endpoint)


@router.get('/route_exists')
def get_endpoint(endpoint: DirectiveFromTo):
    return route_exist(endpoint)
