from managers.Modification.Directive import DirectiveModification


class DirectiveEditor:
    def __init__(self):
        super().__init__()

    def directive_editor(self, main_window, mode, layout, input_line, search_button, add_button, edit_button, delete_button):
        self.search_button = search_button
        self.add_button = add_button
        self.edit_button = edit_button
        self.delete_button = delete_button
        self.main_window = main_window
        self.mode = mode
        self.directive_window = DirectiveModification(main_window)
        self.input_line = input_line
        if self.mode == "search_directive":
            layout.addWidget(self.search_button)
            self.search_button.clicked.connect(lambda: self.directive_window.search_directive(self.input_line))
        elif self.mode == "add_directive":
            layout.addWidget(self.add_button)
            self.add_button.clicked.connect(lambda: self.directive_window.add_record_directive(self.input_line))
        elif self.mode == "edit_directive":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.directive_window.edit_record_directive(self.input_line))
        elif self.mode == "delete_directive":
            layout.addWidget(self.delete_button)
            self.delete_button.clicked.connect(lambda: self.directive_window.delete_record_directive(self.input_line))

    @staticmethod
    def open_search_directive(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'directive', ['Откуда', 'Куда'],
                                  mode="search_directive"))

    @staticmethod
    def open_add_directive(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'directive', ['Откуда', 'Куда'],
                                  mode="add_directive"))

    @staticmethod
    def open_edit_directive(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'directive', ['ID', 'Откуда', 'Куда'],
                                  mode="edit_directive"))

    @staticmethod
    def open_delete_directive(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'directive', ['ID'],
                                  mode="delete_directive"))


directive_editor = DirectiveEditor()
