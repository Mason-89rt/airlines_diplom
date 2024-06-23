from managers.Modification.Subclass_price import SubclassPriceModification


class SubclassPriceEditor:
    def __init__(self):
        super().__init__()

    def subclass_price_editor(self, main_window, mode, layout, input_line, edit_button):
        self.edit_button = edit_button
        self.main_window = main_window
        self.mode = mode
        self.subclass_price_window = SubclassPriceModification(main_window)
        self.input_line = input_line
        if self.mode == "edit_subclass_price":
            layout.addWidget(self.edit_button)
            self.edit_button.clicked.connect(lambda: self.subclass_price_window.edit_record_subclass_price(
                self.input_line))

    @staticmethod
    def open_edit_subclass_price(main_window):
        from TableHandler.TableEditor import TableEditor, editor_window
        editor_window(TableEditor(main_window, 'staff', ['ID', 'price'],
                                  mode="edit_subclass_price"))


subclass_price_editor = SubclassPriceEditor()
