from fastapi import APIRouter
from endpoints.models import Directive
from resolvers.subclass import (get_subclass, get_subclass_description, get_subclass_price, get_description_economy,
                                ticket_price_economy_base, get_description_business, ticket_price_business_base)
router = APIRouter()


@router.get("/subclass")
def get_endpoint():
    return get_subclass()


@router.get("/subclass_price")
def get_endpoint():
    return get_subclass_price()


@router.get("/subclass_description")
def get_endpoint():
    return get_subclass_description()


@router.get('/description_economy')
def get_endpoint():
    return get_description_economy()


@router.get('/ticket_price_economy_base')
def get_endpoint(endpoint: Directive):
    return ticket_price_economy_base(endpoint)


@router.get('/description_business')
def get_endpoint():
    return get_description_business()


@router.get('/ticket_price_business_base')
def get_endpoint(endpoint: Directive):
    return ticket_price_business_base(endpoint)
