from fastapi import APIRouter
from endpoints.models import Directive
from resolvers.class_economy import (ticket_price_economy_base, get_description_economy,
                                     all_class_price_economy_night)

router = APIRouter()


@router.get('/description_economy')
def get_endpoint():
    return get_description_economy()


@router.get('/ticket_price_economy_base')
def get_endpoint(endpoint: Directive):
    return ticket_price_economy_base(endpoint)


@router.get('/all_subclass')
def get_endpoint():
    return all_class_price_economy_night()
