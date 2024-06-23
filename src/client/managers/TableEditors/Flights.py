from managers.Modification.Flights import FlightsModification
from PyQt5.QtWidgets import QCalendarWidget


class FlightsEditor:
    def __init__(self):
        super().__init__()

    def flights_editor(self, main_window, mode, layout, input_line,
                       add_button, edit_button, delete_button):
        # self.search_button = search_button
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        # self.combo_box = combo_box
        # self.button_calendar = button_calendar
        self.main_window = main_window
        self.mode = mode
        self.flights_window = FlightsModification(main_window)
        self.input_line = input_line
        if self.mode == "add_flights":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.flights_window.add_record_flights(self.input_line))
        elif self.mode == "edit_flights":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.flights_window.edit_record_flights(self.input_line))

    def open_add_flights(self, main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'flights', ['Статус рейса', 'Откуда', 'Куда',
                                                           'время начала рейса', 'Время конца рейса', 'Дата рейса',
                                                           'Модель самолета', 'Выход'], mode="add_flights"))

    @staticmethod
    def open_edit_flights(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'flights', ['ID', 'Статус рейса', 'Откуда', 'Куда',
                                                           'время начала рейса', 'Время конца рейса', 'Дата рейса',
                                                           'Модель самолета', 'Выход'],
                                  mode="edit_flights"))


flights_editor = FlightsEditor()
