from API.Information_subclass import get_subclass_information
from TableHandler.TableDataHandler import TableDataHandler


class SubclassDescriptionShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_subclass_description(main_window):
        data = get_subclass_information()
        TableDataHandler.populate_table(main_window.table_subclass_info, data)


subclass_description_show = SubclassDescriptionShow()
