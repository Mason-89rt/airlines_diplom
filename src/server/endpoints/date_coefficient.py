from fastapi import APIRouter
from endpoints.models import DateCoefficientUpdater, DateSearch
from resolvers.date_coefficient import (get_date_coefficient, put_date_coefficient_on_id, get_date_coefficient_on_id,
                                        get_date_coefficient_)
router = APIRouter()


@router.get("/date_coefficient")
def get_endpoint():
    return get_date_coefficient()


@router.get("/date_coefficient_without_id")
def get_endpoint():
    return get_date_coefficient_()


@router.get("/date_")
def get_endpoint(endpoint: DateSearch):
    return get_date_coefficient_on_id(endpoint)


@router.put("/date_coefficient_update")
def put_endpoint(endpoint: DateCoefficientUpdater):
    return put_date_coefficient_on_id(endpoint)
