from API.subclass_price import get_subclass_price
from TableHandler.TableDataHandler import TableDataHandler


class SubclassPriceShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_subclass_price(main_window):
        data = get_subclass_price()
        TableDataHandler.populate_table(main_window.table_subclass_price, data)


subclass_price_show = SubclassPriceShow()
