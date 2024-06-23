from fastapi import APIRouter
from resolvers.gate import get_gate
from endpoints.models import StatusFlight
router = APIRouter()


@router.get("/gate")
def get_endpoint(endpoint: StatusFlight):
    return get_gate(endpoint)
