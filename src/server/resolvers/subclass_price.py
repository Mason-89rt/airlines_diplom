from endpoints.models import SubclassPrice, SubclassPriceUpdater
from db.DBmanager import base_manager


def get_subclass_price():
    res = base_manager.execute("select * from subclass_price", args=())
    subclass_price = []
    for i in res:
        subclass_price.append(SubclassPrice(id=i[0], price=i[1], id_subclass=i[2]))
    return subclass_price


# def post_subclass_price(subclass_price: RoleName):
#     res = base_manager.execute("insert into subclass_price(name) values(?)", args=(subclass_price.name,))
#     return res


def put_subclass_price_on_id(subclass_price: SubclassPriceUpdater):
    res = base_manager.execute("update subclass_price set price=? where id=?", args=(subclass_price.price,
                                                                                     subclass_price.id))
    return res


# def delete_subclass_price(subclass_price: RoleID):
#     res = base_manager.execute("delete from subclass_price where id=?", args=(subclass_price.id,))
#     return res
