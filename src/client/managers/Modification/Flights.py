from API.flights import create_flights, update_flights
from API.gate import get_gate
from API.ticket_info import get_ticket_time_flight
from API.route import get_route
from API.status_flights import get_status
from managers.Show.Flights import flights_show


class FlightsModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def add_record_flights(self, input_line):
        status_flights = input_line[0].text()
        from_ = input_line[1].text()
        to_ = input_line[2].text()
        time_start = input_line[3].text()
        time_end = input_line[4].text()
        date_ = input_line[5].text()
        plane_model = input_line[6].text()
        gate = input_line[7].text()
        if all([status_flights, from_, to_, time_start, time_end, date_, plane_model, gate]):
            create_flights(status_flights, from_, to_, time_start, time_end, date_, plane_model, gate)

        flights_show.show_data_flights(self.main_window)

    def edit_record_flights(self, input_line):
        id_ = input_line[0].text()
        status_flights = input_line[1].text()
        from_ = input_line[2].text()
        to_ = input_line[3].text()
        time_start = input_line[4].text()
        time_end = input_line[5].text()
        date_ = input_line[6].text()
        plane_model = input_line[7].text()
        gate = input_line[8].text()
        if all([id_, status_flights, from_, to_, time_start, time_end, date_, plane_model, gate]):
            update_flights(id_, status_flights, from_, to_, time_start, time_end, date_, plane_model, gate)
        flights_show.show_data_flights(self.main_window)
