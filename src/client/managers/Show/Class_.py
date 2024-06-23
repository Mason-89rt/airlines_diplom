from API.class_ import get_class
from TableHandler.TableDataHandler import TableDataHandler


class ClassShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_class(main_window):
        data = get_class()
        TableDataHandler.populate_table(main_window.table_class, data)


class_show = ClassShow()
