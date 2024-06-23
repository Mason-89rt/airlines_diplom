from modules.ticket_my_flights import TicketMyFlights
from modules.ticket_passenger import TicketPassenger
from client.API.booked_ticket import visible_ticket_book, id_all_in_bookings_seat, delete_seat_book_on_id
from client.API.purchased_ticket import visible_buy_ticket_book, create_buy_ticket


def buy_hide_ticket(ticket):
    ticket.hide()


class VisibleTicket:
    def __init__(self, main_window, id_):
        self.main_window = main_window
        self.id = id_

    def load_booked_tickets(self):
        booked_tickets = visible_ticket_book(self.id)
        buy_tickets = visible_buy_ticket_book(self.id)
        print('Купленные билеты;', buy_tickets)

        if booked_tickets:
            for ticket in booked_tickets:
                self.add_ticket_to_ui(ticket)
        if buy_tickets:
            for ticket in buy_tickets:
                self.add_buying_ticket_to_ui(ticket)

    def add_ticket_to_ui(self, ticket_data):
        ticket = TicketMyFlights()
        ticket.btn_economy_class_13.clicked.connect(
            lambda: self.add_info_buy_booking(ticket, ticket_data))
        ticket.btn_buisness_class_13.clicked.connect(lambda: self.cancel_ticket(ticket, ticket_data))
        ticket.label_time_start_buy_ticket_6.setText(ticket_data[3])
        ticket.label_time_end_buy_ticket_6.setText(ticket_data[4])
        ticket.label_2.setText(ticket_data[0])
        ticket.label_3.setText(ticket_data[1])
        self.main_window.gridLayout_51.addWidget(ticket)
        self.main_window.booked_tickets.append(ticket)
        ticket.show()

    def add_buying_ticket_to_ui(self, ticket_data):
        ticket_passenger = TicketPassenger()
        ticket_passenger.label_time_start_buy_ticket_7.setText(ticket_data[3])
        ticket_passenger.label_14.setText('за 20 минут до вылета')
        ticket_passenger.label_3.setText(ticket_data[1])
        ticket_passenger.label_2.setText(ticket_data[0])
        ticket_passenger.label_time_end_buy_ticket_7.setText(ticket_data[2])
        ticket_passenger.label_9.setText(f"{ticket_data[6]} {ticket_data[7]}")
        ticket_passenger.label_16.setText(f'{ticket_data[8]}')
        ticket_passenger.label_18.setText(f'{ticket_data[9]}')
        ticket_passenger.label_5.setText(ticket_data[5])
        ticket_passenger.label_7.setText(f'{ticket_data[10]}')
        self.main_window.add_info_(ticket_passenger)
        self.main_window.gridLayout_51.addWidget(ticket_passenger)
        self.main_window.bought_tickets.append(ticket_passenger)
        ticket_passenger.show()

    def cancel_ticket(self, ticket, ticket_data):
        if ticket in self.main_window.booked_tickets:
            id_all_bookings_seat = id_all_in_bookings_seat(ticket_data[0], ticket_data[1], ticket_data[2],
                                                           ticket_data[3], ticket_data[4], ticket_data[5], self.id)
            if id_all_bookings_seat is None:
                return False

            delete_booked_ticket = delete_seat_book_on_id(ticket_data[0], ticket_data[1], ticket_data[2],
                                                          ticket_data[3], ticket_data[4], ticket_data[5], self.id)
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

    def add_info_buy_booking(self, ticket, ticket_data):
        if ticket in self.main_window.booked_tickets:
            cancel_result = self.cancel_ticket(ticket, ticket_data)
            if cancel_result:
                create_buy_ticket(self.id, ticket_data[0], ticket_data[1], ticket_data[2], ticket_data[5])
                self.main_window.bought_tickets.append(ticket)
                ticket_passenger = TicketPassenger()
                ticket_passenger.label_time_start_buy_ticket_7.setText(ticket_data[3])
                ticket_passenger.label_14.setText('за 20 минут до вылета')
                ticket_passenger.label_3.setText(ticket_data[1])
                ticket_passenger.label_2.setText(ticket_data[0])
                ticket_passenger.label_time_end_buy_ticket_7.setText(ticket_data[2])
                ticket_passenger.label_9.setText(f"{ticket_data[6]} {ticket_data[7]}")
                ticket_passenger.label_16.setText(f'{ticket_data[8]}')
                ticket_passenger.label_18.setText(f'{ticket_data[9]}')
                ticket_passenger.label_5.setText(ticket_data[5])
                ticket_passenger.label_7.setText(f'{ticket_data[10]}')
                self.main_window.add_info_(ticket_passenger)
                buy_hide_ticket(ticket)


visible_ticket = VisibleTicket(None, None)
