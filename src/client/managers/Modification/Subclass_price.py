from API.subclass_price import put_subclass_price
from managers.Show.Subclass_price import subclass_price_show


class SubclassPriceModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def edit_record_subclass_price(self, input_line):
        id_ = input_line[0].text()
        price = input_line[1].text()
        if id_ and price:
            put_subclass_price(id_, price)
            subclass_price_show.show_data_subclass_price(self.main_window)
