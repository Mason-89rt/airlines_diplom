from fastapi import APIRouter
from resolvers.plane import get_model_plane
from endpoints.models import StatusFlight
router = APIRouter()


@router.get("/model_plane")
def get_endpoint(endpoint: StatusFlight):
    return get_model_plane(endpoint)
