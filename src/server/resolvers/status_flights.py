from db.DBmanager import base_manager
from endpoints.models import StatusFlight


def get_status(status: StatusFlight):
    res = base_manager.execute("""select status from flights_status 
        inner join flights on flights.id_flights_status = flights_status.id
        where flights.id = ?""", args=(status.id_,))
    return res
