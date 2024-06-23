from endpoints.models import SubclassInfo, SubclassInfoUpdater
from db.DBmanager import base_manager


def get_subclass_info():
    res = base_manager.execute("select * from subclass_description", args=())
    subclass_info = []
    for i in res:
        subclass_info.append(SubclassInfo(id=i[0], description=i[1], id_subclass=i[2]))
    return subclass_info


def put_subclass_info_on_id(subclass: SubclassInfoUpdater):
    res = base_manager.execute("update subclass_description set description=? where id=?", args=(subclass.description,
                                                                                                 subclass.id))
    return res
