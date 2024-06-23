from API.staff import (get_staff, get_staff_on_id, get_staff_on_name, get_staff_on_name_surname,
                              get_staff_on_phone, get_staff_on_surname, get_staff_on_id_gender,
                              get_staff_on_id_salary)
from TableHandler.TableDataHandler import TableDataHandler


class StaffShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_staff_on_id(main_window, id_):
        data = get_staff_on_id(id_)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_name(main_window, name):
        data = get_staff_on_name(name)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_name_surname(main_window, name, surname):
        data = get_staff_on_name_surname(name, surname)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_phone(main_window, phone):
        data = get_staff_on_phone(phone)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_surname(main_window, surname):
        data = get_staff_on_surname(surname)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_id_gender(main_window, id_gender):
        data = get_staff_on_id_gender(id_gender)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff_on_id_salary(main_window, id_salary):
        data = get_staff_on_id_salary(id_salary)
        TableDataHandler.populate_table(main_window.table_info_staff, data)

    @staticmethod
    def show_data_staff(main_window):
        data = get_staff()
        TableDataHandler.populate_table(main_window.table_info_staff, data)


staff_show = StaffShow()
