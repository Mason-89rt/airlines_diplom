from API.Information_subclass import put_subclass_information
from managers.Show.Subclass_description import subclass_description_show


class SubclassDescriptionModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def edit_record_subclass_description(self, input_line):
        id_ = input_line[0].text()
        description = input_line[1].text()
        if id_ and description:
            put_subclass_information(id_, description)
            subclass_description_show.show_data_subclass_description(self.main_window)
