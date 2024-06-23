from fastapi import APIRouter
from endpoints.models import GenderDelete
from resolvers.gender import get_gender, delete_gender
router = APIRouter()


@router.get("/gender")
def get_endpoint():
    return get_gender()


@router.delete("/gender_delete")
def delete_endpoint(endpoint: GenderDelete):
    return delete_gender(endpoint)
