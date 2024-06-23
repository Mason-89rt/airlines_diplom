from managers.Modification.Date_coefficient import DateCoefficientModification


class DateCoefficientEditor:
    def __init__(self):
        super().__init__()

    def date_coefficient_editor(self, main_window, mode, layout, input_line, search_button, edit_button):
        self.search_button = search_button
        self.edit_button = edit_button
        self.main_window = main_window
        self.mode = mode
        self.date_coefficient_window = DateCoefficientModification(main_window)
        self.input_line = input_line
        if self.mode == "search_date_coefficient":
            layout.addWidget(self.search_button)
            self.search_button.clicked.connect(lambda: self.date_coefficient_window.search_date(self.input_line))
        elif self.mode == "edit_date_coefficient":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.date_coefficient_window.edit_record_coefficient(self.
                                                                                                          input_line))

    @staticmethod
    def open_search_date_coefficient(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'date_coefficient', ['Date'],
                                  mode="search_date_coefficient"))

    @staticmethod
    def open_edit_date_coefficient(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'date_coefficient', ['ID', 'coefficient'],
                                  mode="edit_date_coefficient"))


date_coefficient_editor = DateCoefficientEditor()
