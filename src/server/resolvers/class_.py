from endpoints.models import Class
from db.DBmanager import base_manager


def get_class():
    res = base_manager.execute("select * from class", args=())
    class_ = []
    for i in res:
        class_.append(Class(id=i[0], name=i[1]))
    return class_


# def post_class(class_: SalaryAmountCreate):
#     res = base_manager.execute("insert into class(amount) values(?)", args=(class_.amount,))
#     return res
#
#
# def put_class_on_id(class_: SalaryAmountUpdater):
#     res = base_manager.execute("update class set amount=? where id=?", args=(class_.amount, class_.id))
#     return res
#
#
# def delete_class(class_: SalaryDelete):
#     res = base_manager.execute("delete from class where id=?", args=(class_.id,))
#     return res
