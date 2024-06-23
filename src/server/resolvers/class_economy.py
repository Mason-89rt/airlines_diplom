from endpoints.models import Directive
from db.DBmanager import base_manager


def get_description_economy():
    res = base_manager.execute("""SELECT DISTINCT subclass_description.description, subclass.name 
    from subclass_description
                                  inner join subclass on subclass.id = subclass_description.id_subclass
                                  INNER JOIN class on class.id = subclass.id_class
                                  inner join date_route on date_route.id_class = class.id
                                  where class.name = 'Эконом'""", args=())
    return res


def ticket_price_economy_base(directive: Directive):
    res = base_manager.execute(
        """SELECT subclass_price.price from subclass_price
inner join subclass on subclass.id = subclass_price.id_subclass
INNER JOIN class on class.id = subclass.id_class
inner join date_route on date_route.id_class = class.id
inner join route on date_route.id_route = route.id
inner join directive on directive.id = route.id_directive
where from_directive = ? and to_directive = ?
and ? = date_route.date_start
and class.name = 'Эконом'""",
        args=(directive.from_directive, directive.to_directive, directive.date_))
    return res


def all_class_price_economy_night():
    res = base_manager.execute("""SELECT DISTINCT subclass.name from subclass""", args=())
    return res


