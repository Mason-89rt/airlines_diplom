from fastapi import APIRouter
from resolvers.class_ import get_class
router = APIRouter()


@router.get("/class")
def get_endpoint():
    return get_class()
