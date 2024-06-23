# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from generated.main_window_ui import Ui_MainWindow
from src.client.API.route import get_route
from src.client.API.ticket_info import (get_price_economy_base_, get_ticket_time_flight, get_price_business_base_,
                                        get_price_subclass_economy, get_price_subclass_business,
                                        calculate_flight_duration, get_id_plane)
from API.subclass import get_description_economy, get_description_business
from API.purchased_ticket import get_seat_buy
from API.seat import get_seat
from API.booked_ticket import get_seat_book
from API.flights import get_number_flights, get_gate_flights
from API.passenger import get_profile_info, put_personal_info, get_profile
from API.user_state import update_user_state
from API.user import get_email
from API.plane import get_model_plane
from API.status_flights import get_status
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from generated.calendar_ui import Ui_calendar
from generated.ui_ticket_add_ui import Ui_Form
from modules.business_class_window import ClassWindowBusiness
from modules.economy_class_window import ClassWindowEconomy
from modules.ticket_status_flight import TicketStatusFlight


class TicketAddWidget(QWidget, Ui_Form):
    def __init__(self, id_):
        super().__init__()
        self.id_ = id_
        self.seat_window = None
        self.setupUi(self)
        self.main_window = None
        self.btn_buisness_class_13.clicked.connect(self.show_prices_business)
        self.btn_economy_class_13.clicked.connect(self.show_prices_economy)
        self.business_window = None
        self.economy_window = None
        self.last_selected_class = None
        self.selected_class = None

    def text_btn(self):
        if self.sender() == self.btn_economy_class_13:
            self.selected_class = 'Эконом'
        elif self.sender() == self.btn_buisness_class_13:
            self.selected_class = 'Бизнес'
        return self.selected_class

    def set_main_window(self, main_window):
        self.main_window = main_window

    def show_prices_business(self):
        selected_class = self.text_btn()
        if self.main_window:
            from_text = self.main_window.line_from_buy_ticket.text()
            to_text = self.main_window.line_to_buy_ticket.text()
            date_from = self.main_window.date_from
            list_prices = get_price_subclass_business(from_text, to_text, date_from)
            description_list = get_description_business()
            time_start = self.label_time_start_buy_ticket_6.text()
            if selected_class:
                self.business_window = ClassWindowBusiness(self.main_window, self.id_,
                                                           self.label_time_start_buy_ticket_6.text(),
                                                           self.label_time_end_buy_ticket_6.text(),
                                                           self.main_window.line_from_buy_ticket.text(),
                                                           self.main_window.line_to_buy_ticket.text(),
                                                           self.main_window.date_from, selected_class)
                if "00:00" <= time_start <= "04:00":
                    for prices, (description, subclass_name), button in zip(list_prices[0][0], description_list,
                                                                            self.business_window.buttons):
                        button.setText(f"Бизнес: {subclass_name}\n\n {description}\n\n Цена: {prices} руб.")
                else:
                    for prices, (description, subclass_name), button in zip(list_prices[1][0], description_list,
                                                                            self.business_window.buttons):
                        button.setText(f"Бизнес: {subclass_name}\n\n {description}\n\n Цена: {prices} руб.")
        self.business_window.show()

    def show_prices_economy(self):
        selected_class = self.text_btn()
        if self.main_window:
            from_text = self.main_window.line_from_buy_ticket.text()
            to_text = self.main_window.line_to_buy_ticket.text()
            date_from = self.main_window.date_from
            list_prices = get_price_subclass_economy(from_text, to_text, date_from)
            description_list = get_description_economy()
            time_start = self.label_time_start_buy_ticket_6.text()
            if selected_class:
                self.economy_window = ClassWindowEconomy(self.main_window, self.id_,
                                                         self.label_time_start_buy_ticket_6.text(),
                                                         self.label_time_end_buy_ticket_6.text(),
                                                         self.main_window.line_from_buy_ticket.text(),
                                                         self.main_window.line_to_buy_ticket.text(),
                                                         self.main_window.date_from, selected_class)
                print(self.id_)
            if "00:00" <= time_start <= "04:00":
                for prices, (description, subclass_name), button in zip(list_prices[0][0], description_list,
                                                                        self.economy_window.buttons):
                    button.setText(f"Эконом: {subclass_name}\n\n {description}\n\n Цена: {prices} руб.")
            else:
                for prices, (description, subclass_name), button in zip(list_prices[1][0], description_list,
                                                                        self.economy_window.buttons):
                    button.setText(f"Эконом: {subclass_name}\n\n {description}\n\n Цена: {prices} руб.")
        self.economy_window.show()


class MainWindowUser(QMainWindow, Ui_MainWindow):
    def __init__(self, id_):
        super().__init__()
        self.to_directive = None
        self.from_directive = None
        self.lbl_not_found_flights = None
        self.dialog = None
        self.date_birthday = None
        self.lbl_no_flights = None
        self.date_from = None
        self.calendar_add_widget = None
        self.setupUi(self)
        self.id = id_
        self.state_no = 'No'
        self.booked_tickets = []
        self.bought_tickets = []
        self.line_from_buy_ticket.setText('Москва')
        self.line_to_buy_ticket.setText('Волгоград')
        self.from_directive = self.line_from_buy_ticket.textChanged.connect(self.format_text)
        self.to_directive = self.line_to_buy_ticket.textChanged.connect(self.format_text)
        self.widget_2.setHidden(True)
        self.data_base_sideboard.deleteLater()
        self.data_base_sideboard_2.deleteLater()
        self.return_directive_buy_ticket.clicked.connect(self.directive_return)
        self.btn_status_flights.clicked.connect(self.status_flight)
        self.sign_out_sideboard.clicked.connect(self.out)
        self.sign_out_sideboard_2.clicked.connect(self.out)
        self.btn_buy_ticket.clicked.connect(self.buy_ticket)
        self.btn_date_flight_buy_ticket.clicked.connect(self.show_calendar)
        self.btn_save.clicked.connect(self.user_data)
        self.pushButton.clicked.connect(self.show_date_profile)
        self.home_sideboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.home_sideboard_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.settings_sideboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settings_sideboard_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.info_sideboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.info_sideboard_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.profile_sideboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.profile_sideboard_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.my_flights_sideboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.my_flights_sideboard_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

    def format_text(self):
        from_text = self.line_from_buy_ticket.text()
        to_text = self.line_to_buy_ticket.text()

        formatted_from_text = from_text.title()
        formatted_to_text = to_text.title()
        if from_text != formatted_from_text:
            cursor_position = self.line_from_buy_ticket.cursorPosition()
            self.line_from_buy_ticket.blockSignals(True)
            self.line_from_buy_ticket.setText(formatted_from_text)
            self.line_from_buy_ticket.setCursorPosition(cursor_position)
            self.line_from_buy_ticket.blockSignals(False)

        if to_text != formatted_to_text:
            cursor_position = self.line_to_buy_ticket.cursorPosition()
            self.line_to_buy_ticket.blockSignals(True)
            self.line_to_buy_ticket.setText(formatted_to_text)
            self.line_to_buy_ticket.setCursorPosition(cursor_position)
            self.line_to_buy_ticket.blockSignals(False)

    def out(self):
        from client.main import MyDialog
        self.close()
        update_user_state(self.id, self.state_no)
        self.dialog = MyDialog()
        self.dialog.show()

    def add_info_(self, child_w):
        self.gridLayout_51.layout().addWidget(child_w)

    def clear_data_profile(self):
        self.line_name_2.clear()
        self.line_surname_2.clear()
        self.pushButton.repaint()
        self.line_phone_2.clear()
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoExclusive(True)

    def fill_data_profile(self):
        data_email = get_email(self.id)
        data = get_profile(self.id)
        if data:
            self.line_name_2.setText(data[0])
            self.line_surname_2.setText(data[1])
            self.line_phone_2.setText(data[3])
            self.pushButton.setText(data[2])
            self.line_email_2.setText(data_email[0])
            if data[4] == 1:
                self.radioButton.setChecked(True)
            elif data[4] == 2:
                self.radioButton_2.setChecked(True)
        else:
            pass

    def fill_data_tickets(self):
        from client.modules.visible_ticket import VisibleTicket
        self.visible_ticket = VisibleTicket(self, self.id)
        self.visible_ticket.load_booked_tickets()

    def user_data(self):
        name = self.line_name_2.text()
        surname = self.line_surname_2.text()
        phone = self.line_phone_2.text()
        date_birthday = self.pushButton.text()
        gender_text = 1 if self.radioButton.isChecked() else 2
        if hasattr(self, 'date_birthday') and self.date_birthday:
            id_gender = int(gender_text)
            e = get_profile_info(name, surname, date_birthday, phone, id_gender, self.id)
            if e is None:
                put_personal_info(name, surname, date_birthday, phone, id_gender, self.id)
            else:
                print("данные не изменены")

    def show_calendar(self):
        self.calendar_add_widget = CalendarAddWidget()
        self.calendar_add_widget.calendarWidget.clicked[QtCore.QDate].connect(self.set_date_on_button)
        self.calendar_add_widget.show()

    def show_date_profile(self):
        self.calendar_add_widget = CalendarAddWidget()
        self.calendar_add_widget.calendarWidget.clicked[QtCore.QDate].connect(self.set_date_on_profile_date)
        self.calendar_add_widget.show()

    def set_date_on_button(self, date):
        self.date_from = date.toString("yyyy-MM-dd")
        self.btn_date_flight_buy_ticket.setText(self.date_from)

    def set_date_on_profile_date(self, date):
        self.date_birthday = date.toString("yyyy-MM-dd")
        self.pushButton.setText(self.date_birthday)

    def buy_ticket(self):
        self.btn_status_flights.setChecked(False)
        self.btn_buy_ticket.setStyleSheet("color: rgb(0, 0, 255);"
                                          "border-bottom: 3px solid blue;")
        self.btn_status_flights.setStyleSheet(" ")
        try:
            self.btn_search_buy_ticket.clicked.disconnect(self.search_status_flight)
        except TypeError:
            pass
        self.btn_search_buy_ticket.clicked.connect(self.open_ticket)

    def status_flight(self):
        self.btn_buy_ticket.setChecked(False)
        self.btn_status_flights.setStyleSheet("color: rgb(0, 0, 255);"
                                              "border-bottom: 3px solid blue;")
        self.btn_buy_ticket.setStyleSheet(" ")
        try:
            self.btn_search_buy_ticket.clicked.disconnect(self.open_ticket)
        except TypeError:
            pass
        self.btn_search_buy_ticket.clicked.connect(self.search_status_flight)

    def open_ticket(self):
        self.clear_tickets()
        self.from_directive = self.line_from_buy_ticket.text()
        self.to_directive = self.line_to_buy_ticket.text()
        if self.from_directive and self.to_directive:
            if hasattr(self, 'date_from') and self.date_from:
                existing_directive = get_route(self.from_directive, self.to_directive, self.date_from)
                if existing_directive is None:
                    self.route_not_found()
                else:
                    self.route_found()
                    self.calendar_add_widget.close()
                    ticket_data = get_ticket_time_flight(self.from_directive, self.to_directive, self.date_from)
                    price_economy = get_price_economy_base_(self.from_directive, self.to_directive, self.date_from)
                    price_business = get_price_business_base_(self.from_directive, self.to_directive, self.date_from)
                    sr_time = calculate_flight_duration(self.from_directive, self.to_directive, self.date_from)
                    self.clear_tickets()
                    print(ticket_data, price_economy, price_business, sr_time)
                    self.add_tickets_day(ticket_data, price_economy, price_business, sr_time)
            else:
                print("Выберите дату.")
        else:
            print("Введите маршрут")

    def search_status_flight(self):
        self.clear_tickets()
        self.from_directive = self.line_from_buy_ticket.text()
        self.to_directive = self.line_to_buy_ticket.text()
        if self.from_directive and self.to_directive:
            if hasattr(self, 'date_from') and self.date_from:
                existing_directive = get_route(self.from_directive, self.to_directive, self.date_from)
                if not existing_directive:
                    self.route_not_found()
                else:
                    self.clear_tickets()
                    self.route_found()
                    ticket_data = get_ticket_time_flight(self.from_directive, self.to_directive, self.date_from)
                    data_gate = get_gate_flights(self.from_directive, self.to_directive)
                    data_model_plane = get_model_plane(existing_directive[0][0])
                    status = get_status(existing_directive[0][0])
                    number = get_number_flights(self.from_directive, self.to_directive)
                    print(ticket_data, data_gate, number, status, data_model_plane)
                    self.add_tickets_status(status, ticket_data, data_gate, data_model_plane, number)
            else:
                print('Введите дату')
        else:
            print("Введите маршрут")

    def route_not_found(self):
        print("Маршрут не найден")
        self.update_route_status(False)

    def route_found(self):
        print("Маршрут найден")
        self.update_route_status(True)

    def update_route_status(self, route_exists):
        if route_exists:
            if self.lbl_not_found_flights is not None:
                self.gridLayout_3.removeWidget(self.lbl_not_found_flights)
                self.lbl_not_found_flights.deleteLater()
                self.lbl_not_found_flights = None
        else:
            self.hide_no_flights_message()
            self.lbl_not_found_flights = QLabel("Маршрут с указанными данными не найден")
            self.lbl_not_found_flights.setFont(QFont('Arial', 20))
            self.lbl_not_found_flights.setAlignment(QtCore.Qt.AlignCenter)
            self.gridLayout_3.addWidget(self.lbl_not_found_flights)
            self.lbl_not_found_flights.setVisible(True)

    def add_tickets_status(self, status, data_time, data_gate, data_model_plane, number_flights):
        for i, (status_flight, time_interval, gate, model_plane, number) in enumerate(zip(status, data_time, data_gate,
                                                                                          data_model_plane,
                                                                                          number_flights)):
            ticket_status = TicketStatusFlight()
            ticket_status.lbl_gate.setFont(QFont('Arial', 14))
            ticket_status.lbl_plane.setFont(QFont('Arial', 14))
            ticket_status.lbl_status.setFont(QFont('Arial', 14))
            ticket_status.lbl_status.setText(status_flight[0])
            ticket_status.lbl_time_start.setText(time_interval[0])
            ticket_status.lbl_time_end.setText(time_interval[1])
            ticket_status.lbl_gate.setText(f'Выход: {gate[0]}')
            ticket_status.lbl_plane.setText(f'Самолет: {model_plane[0]}')
            ticket_status.lbl_airlines_company.setText(f'№{number[0]}')
            self.gridLayout_3.addWidget(ticket_status)

    def add_tickets_day(self, ticket_data_directive, prices_economy, prices_business, sr_time):
        for i, (time_interval, price_economy, price_business, time) in enumerate(
                zip(ticket_data_directive, prices_economy, prices_business, sr_time)):
            ticket_add_widget = TicketAddWidget(self.id)
            ticket_add_widget.label_time_start_buy_ticket_6.setText(time_interval[0])
            ticket_add_widget.label_time_end_buy_ticket_6.setText(time_interval[1])
            ticket_add_widget.btn_economy_class_13.setText(f'Эконом: {str(price_economy)} руб.')
            ticket_add_widget.btn_buisness_class_13.setText(f'Бизнес: {str(price_business)} руб.')
            ticket_add_widget.label.setText(self.line_from_buy_ticket.text())
            ticket_add_widget.label_2.setText(self.line_to_buy_ticket.text())
            ticket_add_widget.sr_time.setText(time)

            id_plane = get_id_plane(self.line_from_buy_ticket.text(), self.line_to_buy_ticket.text(), self.date_from)
            if id_plane is not None:
                all_seat_on_id_plane = get_seat(id_plane)
                if all_seat_on_id_plane is not None:
                    all_booked_seat = True
                    all_buy_seat = True
                    for seat_info in all_seat_on_id_plane:
                        seat_name = seat_info[0]
                        all_booked_seat = get_seat_book(self.line_from_buy_ticket.text(),
                                                        self.line_to_buy_ticket.text(),
                                                        self.date_from, time_interval[0], time_interval[1], seat_name)
                        all_buy_seat = get_seat_buy(self.line_from_buy_ticket.text(), self.line_to_buy_ticket.text(),
                                                    self.date_from, time_interval[0], time_interval[1], seat_name)
                    if all_booked_seat or all_buy_seat:
                        ticket_add_widget.hide()
                        ticket_add_widget.deleteLater()
                        self.show_no_flights_message()
                    else:
                        ticket_add_widget.set_main_window(self)
                        self.gridLayout_3.addWidget(ticket_add_widget)
                        self.hide_no_flights_message()



    def show_no_flights_message(self):
        self.lbl_no_flights = QLabel("Билетов на рейс нет")
        self.lbl_no_flights.setFont(QFont('Arial', 20))
        self.lbl_no_flights.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.lbl_no_flights)
        self.lbl_no_flights.setVisible(True)

    def hide_no_flights_message(self):
        if self.lbl_no_flights is not None:
            self.gridLayout_3.removeWidget(self.lbl_no_flights)
            self.lbl_no_flights.deleteLater()
            self.lbl_no_flights = None

    def clear_tickets(self):
        for i in reversed(range(self.gridLayout_3.count())):
            widget = self.gridLayout_3.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def directive_return(self):
        text_from = self.line_from_buy_ticket.text()
        text_to = self.line_to_buy_ticket.text()
        self.line_from_buy_ticket.setText(text_to)
        self.line_to_buy_ticket.setText(text_from)


class CalendarAddWidget(QWidget, Ui_calendar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
