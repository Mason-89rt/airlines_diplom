from fastapi import APIRouter
from endpoints.models import PlaneID
from db.DBmanager import base_manager

router = APIRouter()


def seat_name(directive: PlaneID):
    res = base_manager.execute("""SELECT DISTINCT seat.name from seat
where id_plane=?""", args=(directive.id,))
    return res


def seat_name_for_economy(economy):
    res = base_manager.execute("""SELECT seat.name from seat inner join class on class.id = seat.id_class 
    where class.name = ?""", args=(economy,))
    return res


def seat_name_for_business(business):
    res = base_manager.execute("""SELECT seat.name from seat inner join class on class.id = seat.id_class 
    where class.name = ?""", args=(business,))
    return res
