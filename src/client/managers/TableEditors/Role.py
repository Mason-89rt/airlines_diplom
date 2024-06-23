class RoleEditor:
    def __init__(self):
        super().__init__()

    def role_editor(self, main_window, mode, layout, input_line, add_button, edit_button, delete_button):
        from managers.Modification.Role import RoleModification
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        self.main_window = main_window
        self.mode = mode
        self.role_window = RoleModification(main_window)
        self.input_line = input_line
        if self.mode == "add_role":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.role_window.add_role(self.input_line))
        elif self.mode == "edit_role":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.role_window.update_role(self.input_line))
        elif self.mode == "delete_role":
            layout.addWidget(self.delete_button)
            self.delete_button.clicked.connect(lambda: self.role_window.delete_role(self.input_line))

    @staticmethod
    def open_edit_role(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(
            TableEditor(main_window, 'role', ['ID', 'name'], mode="edit_role"))

    @staticmethod
    def open_add_role(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'role', ['name'], mode="add_role"))

    @staticmethod
    def open_delete_role(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'role', ['ID'], mode="delete_role"))


role_editor = RoleEditor()
