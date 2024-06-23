from fastapi import APIRouter
from endpoints.models import Directive
from resolvers.class_business import get_description_business, get_price_business_base_night
router = APIRouter()


@router.get('/description_business')
def get_endpoint():
    return get_description_business()


@router.get('/price_business_base_night')
def get_endpoint(endpoint: Directive):
    return get_price_business_base_night(endpoint)
