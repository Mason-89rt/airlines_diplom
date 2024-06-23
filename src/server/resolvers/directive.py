from endpoints.models import (DirectiveShow, DirectiveFromTo, DirectiveFrom, DirectiveTo, DirectiveFromUpdater, DirectiveToUpdater,
                              DirectiveId)
from db.DBmanager import base_manager


def get_directive(directive: DirectiveFromTo):
    res = base_manager.execute("select from_directive, to_directive from directive "
                               "where from_directive=? and to_directive=?",
                               args=(directive.from_directive, directive.to_directive))
    return res


def get_directive_all():
    res = base_manager.execute("select * from directive ", args=())
    directive = []
    for i in res:
        directive.append(DirectiveShow(id=i[0], from_directive=i[1], to_directive=i[2]))
    return directive


def get_directive_from(directive: DirectiveFrom):
    res = base_manager.execute("select * from directive where from_directive=?", args=(directive.from_directive,))
    directive = []
    for i in res:
        directive.append(DirectiveShow(id=i[0], from_directive=i[1], to_directive=i[2]))
    return directive


def get_directive_to(directive: DirectiveTo):
    res = base_manager.execute("select * from directive where to_directive=?", args=(directive.to_directive,))
    directive = []
    for i in res:
        directive.append(DirectiveShow(id=i[0], from_directive=i[1], to_directive=i[2]))
    return directive


def post_directive(directive: DirectiveFromTo):
    res = base_manager.execute("insert into directive(from_directive, to_directive) values(?,?)",
                               args=(directive.from_directive, directive.to_directive))
    return res


def put_directive_to(directive: DirectiveToUpdater):
    res = base_manager.execute("update directive set to_directive=? where id=?",
                               args=(directive.to_directive, directive.id))
    return res


def put_directive_from(directive: DirectiveFromUpdater):
    res = base_manager.execute("update directive set from_directive=? where id=?",
                               args=(directive.from_directive, directive.id))
    return res


def delete_directive(directive: DirectiveId):
    res = base_manager.execute("delete from directive where id=?", args=(directive.id,))
    return res
