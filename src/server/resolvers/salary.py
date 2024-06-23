from endpoints.models import Salary, SalaryAmountUpdater, SalaryAmountCreate, SalaryDelete
from db.DBmanager import base_manager


def get_salary():
    res = base_manager.execute("select * from salary", args=())
    salary = []
    for i in res:
        salary.append(Salary(id=i[0], amount=i[1]))
    return salary


def post_salary(salary: SalaryAmountCreate):
    res = base_manager.execute("insert into salary(amount) values(?)", args=(salary.amount,))
    return res


def put_salary_on_id(salary: SalaryAmountUpdater):
    res = base_manager.execute("update salary set amount=? where id=?", args=(salary.amount, salary.id))
    return res


def delete_salary(salary: SalaryDelete):
    res = base_manager.execute("delete from salary where id=?", args=(salary.id,))
    return res
