from PyQt5.QtWidgets import (QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QApplication, QComboBox,
                             QCalendarWidget)
from PyQt5 import QtCore
from managers.Modification.User import UserModification
from managers.Modification.Staff import StaffModification
from managers.Modification.Role import RoleModification
from managers.Modification.Salary import SalaryModification
from managers.Modification.Subclass_description import SubclassDescriptionModification
from managers.Modification.Directive import DirectiveModification
from managers.Modification.Flights import FlightsModification
from managers.TableEditors.Flights import flights_editor
from managers.TableEditors.Role import role_editor
from managers.TableEditors.User import user_editor
from managers.TableEditors.Staff import staff_editor
from managers.TableEditors.Salary import salary_editor
from managers.TableEditors.Subclass_information import subclass_description_editor
from managers.TableEditors.Subclass_price import subclass_price_editor
from managers.TableEditors.Date_coefficient import date_coefficient_editor
from managers.TableEditors.Directive import directive_editor


def editor_window(editor_windows):
    editor_windows.exec_()


class TableEditor(QDialog):
    def __init__(self, main_window, table_name, fields, mode=''):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle(f'Редактирование таблицы {table_name}')
        self.mode = mode
        # self.line_modification = LineModification()
        self.table_name = table_name
        self.fields = fields

        self.user_window = UserModification(main_window)
        self.staff_window = StaffModification(main_window)
        self.role_window = RoleModification(main_window)
        self.salary_window = SalaryModification(main_window)
        self.flights_window = FlightsModification(main_window)
        self.subclass_description_window = SubclassDescriptionModification(main_window)
        self.directive_window = DirectiveModification(main_window)

        self.input_line = [QLineEdit() for _ in fields]
        self.labels = [QLabel(field) for field in fields]
        self.calendar_button = QPushButton("Select Date")

        self.search_button = QPushButton('Найти')
        self.add_button = QPushButton('Добавить')
        self.edit_button = QPushButton('Изменить')
        self.delete_button = QPushButton('Удалить')

        layout = QVBoxLayout()
        for label, input_field in zip(self.labels, self.input_line):
            layout.addWidget(label)
            layout.addWidget(input_field)

        user_editor.user_editor(main_window, self.mode, layout, self.input_line, self.search_button, self.add_button,
                                self.edit_button, self.delete_button)
        staff_editor.staff_editor(main_window, self.mode, layout, self.input_line, self.search_button, self.add_button,
                                  self.edit_button, self.delete_button)
        role_editor.role_editor(main_window, self.mode, layout, self.input_line, self.add_button, self.edit_button,
                                self.delete_button)
        salary_editor.salary_editor(main_window, self.mode, layout, self.input_line, self.add_button, self.edit_button,
                                    self.delete_button)
        subclass_description_editor.subclass_description_editor(main_window, self.mode, layout, self.input_line,
                                                                self.edit_button)
        subclass_price_editor.subclass_price_editor(main_window, self.mode, layout, self.input_line, self.edit_button)
        date_coefficient_editor.date_coefficient_editor(main_window, self.mode, layout, self.input_line,
                                                        self.search_button, self.edit_button)
        directive_editor.directive_editor(main_window, self.mode, layout, self.input_line, self.search_button,
                                          self.add_button, self.edit_button, self.delete_button)
        flights_editor.flights_editor(main_window, self.mode, layout, self.input_line, self.add_button, self.edit_button,
                                      self.delete_button)
        self.setLayout(layout)


# class LineModification:
#     def __init__(self):
#         super().__init__()
#         self.calendar_add_widget = None
#
#     def show_date_profile(self):
#         self.calendar_add_widget = QCalendarWidget()
#         self.calendar_add_widget.clicked[QtCore.QDate].connect(lambda date: self.set_date_on_button(date))
#         self.calendar_add_widget.show()
#
#     def set_date_on_button(self, date):
#         self.date_from = date.toString("yyyy-MM-dd")
#         print(self.date_from)
#         self.calendar_add_widget.hide()
#
#     def flights_line(self, layout, label, calendar_button):
#         if label.text() == "Откуда":
#             calendar_button.clicked.connect(lambda: self.show_date_profile())
#             layout.addWidget(calendar_button)


if __name__ == '__main__':
    app = QApplication([])
    app.quit()
