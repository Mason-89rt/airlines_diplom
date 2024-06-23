from API.flights import get_flights
from TableHandler.TableDataHandler import TableDataHandler


class FlightsShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_flights(main_window):
        data = get_flights()
        TableDataHandler.populate_table(main_window.table_flights, data)


flights_show = FlightsShow()
