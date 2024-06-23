from API.date_coefficient import get_date_, update_date_coefficient
from managers.Show.Date_coefficient import date_coefficient_show


class DateCoefficientModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def search_date(self, input_line):
        date_ = input_line[0].text()
        if date_:
            get_date_(date_)
            date_coefficient_show.show_data_date_(self.main_window, date_)

    def edit_record_coefficient(self, input_line):
        id_ = input_line[0].text()
        coefficient = input_line[1].text()
        if id_ and coefficient:
            update_date_coefficient(id_, coefficient)
            date_coefficient_show.show_data_date_coefficient(self.main_window)
