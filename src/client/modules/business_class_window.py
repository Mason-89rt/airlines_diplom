from PyQt5.QtWidgets import QDialog, QMessageBox
from generated.business_class_window_ui import UiClassWindowBusiness
from modules.ticket_my_flights import TicketMyFlights
from modules.ticket_passenger import TicketPassenger
from API.ticket_info import calculate_flight_duration
from API.booked_ticket import delete_seat_book_on_id, id_all_in_bookings_seat
from API.flights import get_number_flights, get_gate_flights
from API.purchased_ticket import create_buy_ticket

from modules.choice_seat import SeatWidget


def buy_hide_ticket(ticket):
    ticket.hide()


class ClassWindowBusiness(QDialog, UiClassWindowBusiness):
    def __init__(self, main_window_, id_, time_start, time_end, from_, to_, date_, class_name):
        super().__init__()
        self.name_ = None
        self.surname_ = None
        self.child_ = TicketMyFlights()
        self.id_ = id_
        self.child_w = None
        self.setupUi(self)
        self.buttons = [self.btn_base_bus, self.btn_standart_bus, self.btn_plus_bus]
        self.current_button = None
        self.main_window = main_window_
        self.time_start = time_start
        self.time_end = time_end
        self.from_ = from_
        self.class_name = class_name
        self.to_ = to_
        self.date_ = date_
        self.seat_window = SeatWidget(self, self.id_, self.from_, self.to_, self.date_, self.time_start, self.time_end,
                                      self.class_name)

        self.number_flights = get_number_flights(self.from_, self.to_)
        self.gate_flights = get_gate_flights(self.from_, self.to_)
        self.sr_time = calculate_flight_duration(self.from_, self.to_, self.date_)
        self.pushButton_2.clicked.connect(self.open_seat_booking)
        self.ticket_purchased = False
        for button in self.buttons:
            button.clicked.connect(self.set_button_style)

    def open_seat_booking(self):
        if self.current_button is None:
            QMessageBox.warning(self, "Предупреждение", "Выберите класс")
            return
        self.name_ = self.main_window.line_name_2.text()
        self.surname_ = self.main_window.line_surname_2.text()
        if not self.name_ or not self.surname_:
            QMessageBox.warning(self, "Предупреждение", "Для начала введите данные во вкладке `Мой профиль`")
            return
        self.seat_window.show()

    def add_info(self, seat_name):
        child = TicketMyFlights()
        child.btn_economy_class_13.clicked.connect(lambda: self.add_info_buy_booking(child, seat_name))
        child.btn_buisness_class_13.clicked.connect(lambda: self.cancel_ticket(child, seat_name))
        child.label_time_start_buy_ticket_6.setText(self.time_start)
        child.label_time_end_buy_ticket_6.setText(self.time_end)
        child.label_2.setText(self.from_)
        child.label_3.setText(self.to_)
        child.sr_time.setText(f'{self.sr_time[0]}')
        self.main_window.add_info_(child)
        self.main_window.booked_tickets.append(child)
        QMessageBox.information(self, "Информация",
                                """Билет забронирован, вы можете его купить или отменить во вкладке `Мои рейсы`""")
        child.show()
        self.close()
    def cancel_ticket(self, ticket, seat_name):
        if ticket in self.main_window.booked_tickets:
            id_all_bookings_seat = id_all_in_bookings_seat(self.from_, self.to_, self.date_, self.time_start,
                                                           self.time_end, seat_name, self.id_)
            if not id_all_bookings_seat:
                return False

            delete_booked_ticket = delete_seat_book_on_id(self.from_, self.to_, self.date_, self.time_start,
                                                          self.time_end, seat_name, self.id_)
            if delete_booked_ticket:
                print("Удаление успешное")
                self.main_window.booked_tickets.remove(ticket)
                self.main_window.gridLayout_51.removeWidget(ticket)
                ticket.deleteLater()
                buy_hide_ticket(ticket)
                return True
            else:
                print("Удаление неудачное")
                return False
    def add_info_buy_booking(self, ticket, seat_name):
        if ticket in self.main_window.booked_tickets:
            cancel_result = self.cancel_ticket(ticket, seat_name)
            if cancel_result:
                create_buy_ticket(self.id_, self.from_, self.to_, self.date_, seat_name)
                self.main_window.bought_tickets.append(ticket)
                self.name_ = self.main_window.line_name_2.text()
                self.surname_ = self.main_window.line_surname_2.text()
                ticket_passenger = TicketPassenger()
                ticket_passenger.label_time_start_buy_ticket_7.setText(self.time_start)
                ticket_passenger.label_14.setText('за 20 минут до вылета')
                ticket_passenger.label_3.setText(self.from_)
                ticket_passenger.label_2.setText(self.to_)
                ticket_passenger.label_time_end_buy_ticket_7.setText(self.date_)
                ticket_passenger.label_9.setText(f"{self.name_} {self.surname_}")
                ticket_passenger.label_16.setText(f'{self.number_flights[0]}')
                ticket_passenger.label_18.setText(f'{self.gate_flights[0]}')
                ticket_passenger.label_5.setText(seat_name)
                ticket_passenger.label_7.setText(f'{self.class_name}')
                QMessageBox.information(self, "Информация",
                                        "Билет куплен, информация о нем находится во вкладке `Мои рейсы`")
                self.main_window.add_info_(ticket_passenger)
                self.close()
                buy_hide_ticket(ticket)

    def add_info_buy(self, seat_name):
        ticket_passenger = TicketPassenger()
        ticket_passenger.label_time_start_buy_ticket_7.setText(self.time_start)
        ticket_passenger.label_14.setText('за 20 минут до вылета')
        ticket_passenger.label_3.setText(self.from_)
        ticket_passenger.label_2.setText(self.to_)
        ticket_passenger.label_time_end_buy_ticket_7.setText(self.date_)
        ticket_passenger.label_9.setText(f"{self.name_} {self.surname_}")
        ticket_passenger.label_16.setText(f'{self.number_flights[0]}')
        ticket_passenger.label_18.setText(f'{self.gate_flights[0]}')
        ticket_passenger.label_5.setText(seat_name)
        ticket_passenger.label_7.setText(f'{self.class_name}')
        QMessageBox.information(self, "Информация",
                                "Билет куплен, информация о нем находится во вкладке `Мои рейсы`")
        self.main_window.add_info_(ticket_passenger)
        self.close()

    def set_button_style(self):
        sender = self.sender()
        self.current_button = sender
        for button in self.buttons:
            button.setStyleSheet("")
        sender.setStyleSheet("""
                            QPushButton {
                                color: rgb(0, 0, 255);
                                background-color: rgb(255, 255, 255);
                                border: 3px solid blue;
                            }
                        """)
