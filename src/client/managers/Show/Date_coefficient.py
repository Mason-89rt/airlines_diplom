from API.date_coefficient import get_date_coefficient, get_date_
from TableHandler.TableDataHandler import TableDataHandler


class DateCoefficientShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_date_coefficient(main_window):
        data = get_date_coefficient()
        TableDataHandler.populate_table(main_window.table_coefficient, data)

    @staticmethod
    def show_data_date_(main_window, date_):
        data = get_date_(date_)
        TableDataHandler.populate_table(main_window.table_coefficient, data)


date_coefficient_show = DateCoefficientShow()
