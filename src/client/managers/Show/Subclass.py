from client.API.subclass import get_subclass
from TableHandler.TableDataHandler import TableDataHandler


class SubclassShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_subclass(main_window):
        data = get_subclass()
        TableDataHandler.populate_table(main_window.table_subclass, data)


subclass_show = SubclassShow()
