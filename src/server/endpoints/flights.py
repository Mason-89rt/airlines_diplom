from fastapi import APIRouter
from endpoints.models import DirectiveFromTo, FlightsCreate, FlightsUpdate
from resolvers.flights import get_gate, get_number_flight, insert_flights, update_flights, get_flights
router = APIRouter()


@router.get('/flights')
def get_endpoint():
    return get_flights()


@router.get('/gate_flights')
def get_endpoint(endpoint: DirectiveFromTo):
    return get_gate(endpoint)


@router.get('/number_flights')
def get_endpoint(endpoint: DirectiveFromTo):
    return get_number_flight(endpoint)


@router.post('/flights_create')
def post_endpoint(endpoint: FlightsCreate):
    return insert_flights(endpoint)


@router.put('/flights_update')
def post_endpoint(endpoint: FlightsUpdate):
    return update_flights(endpoint)
