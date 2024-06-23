from fastapi import APIRouter
from endpoints.models import SubclassPriceUpdater
from resolvers.subclass_price import get_subclass_price, put_subclass_price_on_id
router = APIRouter()


@router.get("/subclass_price")
def get_endpoint():
    return get_subclass_price()


@router.put("/subclass_price_update")
def put_endpoint(endpoint: SubclassPriceUpdater):
    return put_subclass_price_on_id(endpoint)


# @router.post("/new_subclass_price")
# def post_endpoint(endpoint: RoleName):
#     return post_role(endpoint)


# @router.delete("/subclass_price_delete")
# def delete_endpoint(endpoint: RoleID):
#     return delete_subclass_price(endpoint)
