from managers.Modification.Staff import StaffModification


class StaffEditor:
    def __init__(self):
        super().__init__()

    def staff_editor(self, main_window, mode, layout, input_line, search_button, add_button, edit_button, delete_button):
        self.search_button = search_button
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        self.main_window = main_window
        self.mode = mode
        self.staff_window = StaffModification(main_window)
        self.input_line = input_line
        if self.mode == "search_staff":
            layout.addWidget(self.search_button)
            self.search_button.clicked.connect(lambda: self.staff_window.search_staff(self.input_line))
        elif self.mode == "add_staff":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.staff_window.add_staff(self.input_line))
        elif self.mode == "edit_staff":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.staff_window.edit_record(self.input_line))
        elif self.mode == "delete_staff":
            layout.addWidget(self.delete_button)
            self.delete_button.clicked.connect(lambda: self.staff_window.delete_record(self.input_line))

    @staticmethod
    def open_search_staff(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'staff', ['ID', 'name', 'surname', 'phone', 'gender_id', 'id_salary'],
                                  mode="search_staff"))

    @staticmethod
    def open_add_staff(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'staff', ['name', 'surname', 'phone', 'gender_id', 'id_salary'],
                                  mode="add_staff"))

    @staticmethod
    def open_edit_staff(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'staff', ['ID', 'name', 'surname', 'phone', 'gender_id', 'id_salary'],
                                  mode="edit_staff"))

    @staticmethod
    def open_delete_staff(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'staff', ['ID'],
                                  mode="delete_staff"))


staff_editor = StaffEditor()

