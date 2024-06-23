from endpoints.models import Subclass, Directive
from db.DBmanager import base_manager


def get_subclass():
    res = base_manager.execute("select * from subclass", args=())
    return res


def get_subclass_price():
    res = base_manager.execute("select price from subclass", args=())
    return res


def get_subclass_description():
    res = base_manager.execute("select description from subclass", args=())
    return res


def get_description_economy():
    res = base_manager.execute("""SELECT DISTINCT description, subclass.name 
    from subclass
    INNER JOIN class on class.id = subclass.id_class
    where class.name = 'Эконом'""", args=())
    return res


def ticket_price_economy_base(directive: Directive):
    res = base_manager.execute(
        """SELECT DISTINCT subclass.price from subclass
INNER JOIN class on class.id = subclass.id_class
inner join route on route.id_directive = directive.id
inner join directive on directive.id = route.id_directive
inner join flights on flights.id_date_ = date_route.id
inner join date_route on date_route.id = flights.id_date_
where from_directive = ? and to_directive = ? and date_route.date_start = ?
and class.name = 'Эконом'""",
        args=(directive.from_directive, directive.to_directive, directive.date_))
    return res


def get_description_business():
    res = base_manager.execute("""SELECT DISTINCT description, subclass.name 
    from subclass
    INNER JOIN class on class.id = subclass.id_class
    where class.name = 'Бизнес'""", args=())
    return res


def ticket_price_business_base(directive: Directive):
    res = base_manager.execute(
        """SELECT DISTINCT subclass.price from subclass
INNER JOIN class on class.id = subclass.id_class
inner join route on route.id_directive = directive.id
inner join directive on directive.id = route.id_directive
inner join flights on flights.id_date_ = date_route.id
inner join date_route on date_route.id = flights.id_date_
where from_directive = ? and to_directive = ? and date_route.date_start = ?
and class.name = 'Бизнес'""",
        args=(directive.from_directive, directive.to_directive, directive.date_))
    return res
