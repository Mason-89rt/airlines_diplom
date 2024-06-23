class UserEditor:
    def __init__(self):
        super().__init__()

    def user_editor(self, main_window, mode, layout, input_line, search_button, add_button, edit_button, delete_button):
        from managers.Modification.User import UserModification
        self.search_button = search_button
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        self.main_window = main_window
        self.mode = mode
        self.user_window = UserModification(main_window)
        self.input_line = input_line
        if self.mode == "add_user":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.user_window.add_record(self.input_line))
        elif self.mode == "edit_user":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.user_window.edit_record(self.input_line))
        elif self.mode == "delete_user":
            layout.addWidget(self.delete_button)
            self.delete_button.clicked.connect(lambda: self.user_window.delete_record(self.input_line))
        elif self.mode == "search_user":
            layout.addWidget(self.search_button)
            self.search_button.clicked.connect(lambda: self.user_window.search_user(self.input_line))

    @staticmethod
    def open_edit(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(
            TableEditor(main_window, 'users', ['ID', 'login', 'password', 'email', 'role_id'], mode="edit_user"))

    @staticmethod
    def open_search(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'users', ['ID', 'login', 'password', 'email'],
                                  mode="search_user"))

    @staticmethod
    def open_add(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'users', ['login', 'password', 'email'], mode="add_user"))

    @staticmethod
    def open_delete(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'users', ['ID'], mode="delete_user"))


user_editor = UserEditor()

