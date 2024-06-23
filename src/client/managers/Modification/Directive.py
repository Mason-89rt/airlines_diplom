from API.directive import (get_directive_from, get_directive_to, update_directive_from, update_directive_to,
                           delete_directive, create_directive)
from API.route import route_exists
from managers.Show.Directive import directive_show
from PyQt5.QtWidgets import QMessageBox
import pycountry
import re
import urllib.parse
import aiohttp
import asyncio

class DirectiveModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def validate_location(self, location):
        return self.validate_city_or_country(location)

    def validate_city_or_country(self, name):
        if len(name.strip()) < 3:
            return False

        if not re.match(r"^[а-яА-Я\s\-]+$", name):
            return False

        if self.validate_country(name):
            return True

        return asyncio.run(self.validate_location_via_api(name))

    def validate_country(self, country_name):
        countries = [country.name for country in pycountry.countries]
        return country_name in countries

    async def validate_location_via_api(self, location):
        api_key = '85dd94e7750340658f06bd1eb0b9e0c3'
        encoded_location = urllib.parse.quote(location)
        url = f"https://api.opencagedata.com/geocode/v1/json?q={encoded_location}&key={api_key}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return len(data['results']) > 0

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
            if self.validate_location(from_) and self.validate_location(to_):
                QMessageBox.information(None, "info", "Маршрут верный!")
                if route_exists(from_, to_):
                    QMessageBox.warning(None, "info", "Маршрут существует")
                else:
                    create_directive(from_, to_)
            else:
                QMessageBox.warning(None, "Error", """Неверная валидация локации! Пожалуйста введите валидное 
                название города или страны.""")
        directive_show.show_data_directive(self.main_window)

    def edit_record_directive(self, input_line):
        id_ = input_line[0].text()
        from_ = input_line[1].text()
        to_ = input_line[2].text()
        if id_ and to_ and from_:
            if self.validate_location(from_) and self.validate_location(to_):
                QMessageBox.information(None, "info", "Маршрут верный!")
                if route_exists(from_, to_):
                    QMessageBox.warning(None, "info", "Маршрут существует")
                else:
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
