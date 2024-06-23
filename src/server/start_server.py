import uvicorn
from fastapi import FastAPI
from endpoints.passenger import router as router_passenger
from endpoints.user import router as router_users
from endpoints.directive import router as router_directive
from endpoints.route import router as router_route
from endpoints.ticket_time import router as ticket_route
from endpoints.class_business import router as description_business_route
from endpoints.class_economy import router as description_economy_route
from endpoints.flights import router as flights_route
from endpoints.staff import router as router_staff
from endpoints.bookings import router as router_bookings
from endpoints.role import router as router_role
from endpoints.gender import router as router_gender
from endpoints.salary import router as router_salary
from endpoints.class_ import router as router_class
from endpoints.subclass import router as router_subclass
from endpoints.information_subclass import router as router_subclass_information
from endpoints.date_coefficient import router as router_date_coefficient
from endpoints.subclass_price import router as subclass_price
from endpoints.user_getpass import router as router_user_getpass
from endpoints.user_state import router as router_user_state
from endpoints.status_flights import router as router_status_flights
from endpoints.plane import router as router_plane
from endpoints.gate import router as router_gate
from endpoints.purchased_ticket import router as router_purchased_ticket
from endpoints.seat import router as router_seat
from db.DBmanager import base_manager


app = FastAPI()


app.include_router(router_users, prefix='/users_start')
app.include_router(router_passenger, prefix='/passenger_start')
app.include_router(router_staff, prefix='/staff_start')
app.include_router(router_bookings, prefix='/bookings_start')
app.include_router(router_purchased_ticket, prefix='/purchased_ticket_start')
app.include_router(router_role, prefix='/role_start')
app.include_router(router_gender, prefix='/gender_start')
app.include_router(router_salary, prefix='/salary_start')
app.include_router(router_class, prefix='/class_start')
app.include_router(subclass_price, prefix='/subclass_price_start')
app.include_router(router_subclass, prefix='/subclass_start')
app.include_router(router_subclass_information, prefix='/subclass_information_start')
app.include_router(router_date_coefficient, prefix='/date_coefficient_start')
app.include_router(router_user_getpass, prefix='/user_getpass_start')
app.include_router(router_status_flights, prefix='/start_status_flights')
app.include_router(router_plane, prefix='/model_plane_start')
app.include_router(router_user_state, prefix='/user_state')
app.include_router(router_gate, prefix='/gate_start')
app.include_router(router_directive, prefix='/directive_start')
app.include_router(router_route, prefix='/route_start')
app.include_router(ticket_route, prefix='/ticket_start')
app.include_router(description_business_route, prefix='/description_business_start')
app.include_router(description_economy_route, prefix='/description_economy_start')
app.include_router(flights_route, prefix='/flights_start')
app.include_router(router_seat, prefix='/seat_start')


@app.get('/')
def start_page():
    return 'Page BD'


if __name__ == "__main__":
    if not base_manager.check_base():
        base_manager.initialize()
    else:
        print("База данных создана")
    uvicorn.run(app, host="0.0.0.0", port=8000)
