from fastapi import APIRouter
from endpoints.models import PlaneID
from resolvers.seat import seat_name, seat_name_for_economy, seat_name_for_business

router = APIRouter()


@router.get('/seat_name')
def get_endpoint(endpoint: PlaneID):
    return seat_name(endpoint)


@router.get('/seat_name_for_economy')
def get_endpoint(economy):
    return seat_name_for_economy(economy)


@router.get('/seat_name_for_business')
def get_endpoint(business):
    return seat_name_for_business(business)
