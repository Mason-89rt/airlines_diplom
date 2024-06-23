from db.DBmanager import base_manager
from endpoints.models import StatusFlight


def get_model_plane(status: StatusFlight):
    res = base_manager.execute("""select name from model
        inner join plane on plane.id_model = model.id  
        inner join flights on flights.id_plane = plane.id
        inner join route on route.id = flights.id_route
        inner join directive on directive.id = route.id_directive
        where flights.id = ?""", args=(status.id_,))
    return res
