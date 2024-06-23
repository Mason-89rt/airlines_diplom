from API.directive import (get_directive_from, get_directive_to, update_directive_from, update_directive_to,
                                  delete_directive, create_directive)
from managers.Show.Directive import directive_show
from PyQt5.QtWidgets import QMessageBox


class DirectiveModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def search_directive(self, input_line):
        from_ = input_line[0].text()
        to_ = input_line[1].text()
        if from_:
            get_directive_from(from_)
            directive_show.show_data_directive_from(self.main_window, from_)
        elif to_:
            get_directive_to(to_)
            directive_show.show_data_directive_to(self.main_window, to_)

    def add_record_directive(self, input_line):
        from_ = input_line[0].text()
        to_ = input_line[1].text()
        if from_ and to_:
            create_directive(from_, to_)
        directive_show.show_data_directive(self.main_window)

    def edit_record_directive(self, input_line):
        id_ = input_line[0].text()
        from_ = input_line[1].text()
        to_ = input_line[2].text()
        if id_ and from_:
            update_directive_from(id_, from_)
        if id_ and to_:
            update_directive_to(id_, to_)
        if id_ and to_ and from_:
            update_directive_to(id_, to_)
            update_directive_from(id_, from_)
        directive_show.show_data_directive(self.main_window)

    def delete_record_directive(self, input_line):
        fields_data = [input_field.text() for input_field in input_line]
        if all(fields_data):
            id_ = int(fields_data[0])
            try:
                id_ = int(id_)
                if id_ <= 0:
                    QMessageBox.warning(None, "Предупреждение", "должно быть положительное число")
                    return
                delete_directive(id_)
                print("Направление удален")
            except ValueError:
                QMessageBox.warning(None, "Предупреждение", "Введите корректное число.")
        else:
            print("Введите идентификатор персонала который нужно удалить.")
        directive_show.show_data_directive(self.main_window)
