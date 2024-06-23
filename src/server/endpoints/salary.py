from fastapi import APIRouter
from endpoints.models import SalaryAmountUpdater, SalaryAmountCreate, SalaryDelete
from resolvers.salary import get_salary, post_salary, put_salary_on_id, delete_salary
router = APIRouter()


@router.get("/salary")
def get_endpoint():
    return get_salary()


@router.put("/salary_update")
def put_endpoint(endpoint: SalaryAmountUpdater):
    return put_salary_on_id(endpoint)


@router.post("/new_salary")
def post_endpoint(endpoint: SalaryAmountCreate):
    return post_salary(endpoint)


@router.delete("/salary_delete")
def delete_endpoint(endpoint: SalaryDelete):
    return delete_salary(endpoint)
