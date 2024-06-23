from API.directive import (get_directive_all, get_directive_from, get_directive_to)
from TableHandler.TableDataHandler import TableDataHandler


class DirectiveShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_directive(main_window):
        data = get_directive_all()
        TableDataHandler.populate_table(main_window.table_directive, data)

    @staticmethod
    def show_data_directive_to(main_window, to_):
        data = get_directive_to(to_)
        TableDataHandler.populate_table(main_window.table_directive, data)

    @staticmethod
    def show_data_directive_from(main_window, from_):
        data = get_directive_from(from_)
        TableDataHandler.populate_table(main_window.table_directive, data)


directive_show = DirectiveShow()
