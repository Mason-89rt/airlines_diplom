from API.gender import get_gender
from TableHandler.TableDataHandler import TableDataHandler


class GenderShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_gender(main_window):
        data = get_gender()
        TableDataHandler.populate_table(main_window.table_gender, data)


gender_show = GenderShow()
