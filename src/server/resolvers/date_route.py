from db.DBmanager import base_manager
from fastapi import APIRouter
from endpoints.models import DateFrom

router = APIRouter()


def get_ticket_date_directive(date_: DateFrom):
    res = base_manager.execute("SELECT directive.from_directive,directive.to_directive, date_route.date_from "
                               "FROM date_route " 
                               "INNER JOIN directive ON directive.id = route.id_directive "
                               "INNER JOIN route ON route.id_date_route = date_route.id "
                               "WHERE route.route_type=1 and date_route.date_from = ? ",
                               args=(date_.date_from,), many=True)
    return res
