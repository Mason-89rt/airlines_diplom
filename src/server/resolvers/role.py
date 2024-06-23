from endpoints.models import Role, RoleName, RoleID
from db.DBmanager import base_manager


def get_role():
    res = base_manager.execute("select * from role", args=())
    role = []
    for i in res:
        role.append(Role(id=i[0], name=i[1]))
    return role


def post_role(role: RoleName):
    res = base_manager.execute("insert into role(name) values(?)", args=(role.name,))
    return res


def put_role_on_id(role: Role):
    res = base_manager.execute("update role set name=? where id=?", args=(role.name, role.id))
    return res


def delete_role(role: RoleID):
    res = base_manager.execute("delete from role where id=?", args=(role.id,))
    return res
