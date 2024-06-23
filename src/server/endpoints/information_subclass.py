from fastapi import APIRouter
from endpoints.models import SubclassInfoUpdater
from resolvers.information_subclass import get_subclass_info, put_subclass_info_on_id
router = APIRouter()


@router.get("/subclass_description")
def get_endpoint():
    return get_subclass_info()


@router.put("/subclass_description_update")
def put_endpoint(endpoint: SubclassInfoUpdater):
    return put_subclass_info_on_id(endpoint)
