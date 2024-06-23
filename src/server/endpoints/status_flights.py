from fastapi import APIRouter
from resolvers.status_flights import get_status
from endpoints.models import StatusFlight
router = APIRouter()


@router.get("/status")
def get_endpoint(endpoint: StatusFlight):
    return get_status(endpoint)
