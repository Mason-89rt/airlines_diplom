from managers.Modification.Salary import SalaryModification


class SalaryEditor:
    def __init__(self):
        super().__init__()

    def salary_editor(self, main_window, mode, layout, input_line, add_button, edit_button, delete_button):
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        self.main_window = main_window
        self.mode = mode
        self.salary_window = SalaryModification(main_window)
        self.input_line = input_line
        if self.mode == "add_salary":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.salary_window.add_salary(self.input_line))
        elif self.mode == "edit_salary":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.salary_window.update_salary(self.input_line))
        elif self.mode == "delete_salary":
            layout.addWidget(self.delete_button)
            self.delete_button.clicked.connect(lambda: self.salary_window.delete_salary(self.input_line))

    @staticmethod
    def open_add_salary(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'salary', ['amount'],
                                  mode="add_salary"))

    @staticmethod
    def open_edit_salary(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'salary', ['ID', 'amount'],
                                  mode="edit_salary"))

    @staticmethod
    def open_delete_salary(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'salary', ['ID'],
                                  mode="delete_salary"))


salary_editor = SalaryEditor()
