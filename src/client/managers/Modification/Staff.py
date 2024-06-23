from API.staff import (get_staff_on_id, get_staff_on_phone, get_staff_on_surname,
                              get_staff_on_name_surname, get_staff_on_id_gender, get_staff_on_id_salary,
                              get_staff_on_name, put_staff_name, put_staff_id_gender, put_staff_id_salary,
                              put_staff_surname, put_staff_phone, delete_staff_id, post_staff)
from managers.Show.Staff import staff_show
from PyQt5.QtWidgets import QMessageBox


class StaffModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def search_staff(self, input_line):
        id_ = input_line[0].text()
        name = input_line[1].text()
        surname = input_line[2].text()
        phone = input_line[3].text()
        id_gender = input_line[4].text()
        id_salary = input_line[5].text()
        if name and surname:
            get_staff_on_name_surname(name, surname)
            staff_show.show_data_staff_on_name_surname(self.main_window, name, surname)
        elif id_:
            get_staff_on_id(id_)
            staff_show.show_data_staff_on_id(self.main_window, id_)
        elif name:
            get_staff_on_name(name)
            staff_show.show_data_staff_on_name(self.main_window, name)
        elif surname:
            get_staff_on_surname(surname)
            staff_show.show_data_staff_on_surname(self.main_window, surname)
        elif phone:
            get_staff_on_phone(phone)
            staff_show.show_data_staff_on_phone(self.main_window, phone)
        elif id_gender:
            get_staff_on_id_gender(id_gender)
            staff_show.show_data_staff_on_id_gender(self.main_window, id_gender)
        elif id_salary:
            get_staff_on_id_salary(id_salary)
            staff_show.show_data_staff_on_id_salary(self.main_window, id_salary)

    def edit_record(self, input_line):
        id_ = input_line[0].text()
        name = input_line[1].text()
        surname = input_line[2].text()
        phone = input_line[3].text()
        id_gender = input_line[4].text()
        id_salary = input_line[5].text()
        if id_ and name:
            put_staff_name(id_, name)
            print("Имя обновлено")
        if id_ and surname:
            put_staff_surname(id_, surname)
            print("Фамилия обновлена")
        if id_ and phone:
            put_staff_phone(id_, phone)
            print("Телефон обновлен")
        if id_ and id_gender:
            try:
                id_gender = int(id_gender)
                if id_gender <= 0:
                    QMessageBox.warning(None, "Предупреждение", "должно быть положительное число")
                    return
                put_staff_id_gender(id_, id_gender)
                print("Пол обновлен")
            except ValueError:
                QMessageBox.warning(None, "Предупреждение", "Введите корректное число.")
        if id_ and id_salary:
            try:
                id_salary = int(id_salary)
                if id_salary <= 0:
                    QMessageBox.warning(None, "Предупреждение", "Зарплата должна быть положительным числом")
                    return
                put_staff_id_salary(id_, id_salary)
                print("Зарплата обновлена")
            except ValueError:
                QMessageBox.warning(None, "Предупреждение", "Введите корректное число для зарплаты.")
        staff_show.show_data_staff(self.main_window)

    def add_staff(self, input_line):
        name = input_line[0].text()
        surname = input_line[1].text()
        phone = input_line[2].text()
        id_gender = input_line[3].text()
        id_salary = input_line[4].text()
        if name and surname and phone and id_gender and id_salary:
            post_staff(name, surname, phone, id_gender, id_salary)
        else:
            QMessageBox.information(None, "Информация", "Введите все данные для создания персонала")
        staff_show.show_data_staff(self.main_window)

    def delete_record(self, input_line):
        fields_data = [input_field.text() for input_field in input_line]
        if all(fields_data):
            id_ = int(fields_data[0])
            try:
                id_ = int(id_)
                if id_ <= 0:
                    QMessageBox.warning(None, "Предупреждение", "должно быть положительное число")
                    return
                delete_staff_id(id_)
                print("Персонал удален")
            except ValueError:
                QMessageBox.warning(None, "Предупреждение", "Введите корректное число.")
        else:
            print("Введите идентификатор персонала который нужно удалить.")
        staff_show.show_data_staff(self.main_window)
