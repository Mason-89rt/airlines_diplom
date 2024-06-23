from fastapi import APIRouter
from endpoints.models import Role, RoleName, RoleID
from resolvers.role import get_role, put_role_on_id, post_role, delete_role
router = APIRouter()


@router.get("/roles")
def get_endpoint():
    return get_role()


@router.put("/role_update")
def put_endpoint(endpoint: Role):
    return put_role_on_id(endpoint)


@router.post("/new_role")
def post_endpoint(endpoint: RoleName):
    return post_role(endpoint)


@router.delete("/role_delete")
def delete_endpoint(endpoint: RoleID):
    return delete_role(endpoint)
