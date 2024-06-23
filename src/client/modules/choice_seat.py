from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout
from API.ticket_info import get_id_plane
from API.purchased_ticket import get_seat_buy, create_buy_ticket
from API.seat import get_seat
from API.booked_ticket import create_seat_book, get_seat_book
from API.seat import get_seat_name_for_business, get_seat_name_for_economy
import sys


class SeatWidget(QWidget):
    def __init__(self, main_window_, id_, from_, to_, date_, t_s, t_e, class_name):
        super().__init__()
        self.selected_seat = None
        self.time_start = t_s
        self.time_end = t_e
        self.id_ = id_
        self.from_ = from_
        self.to_ = to_
        self.class_name = class_name
        self.date_ = date_
        self.main_window_ = main_window_
        self.id_plane = get_id_plane(self.from_, self.to_, self.date_)
        self.seats = get_seat(self.id_plane)
        self.seats_economy = get_seat_name_for_economy('Эконом')
        self.seats_business = get_seat_name_for_business('Бизнес')
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.create_seat_buttons(grid_layout, self.seats_economy, "green", "Эконом")
        self.create_seat_buttons(grid_layout, self.seats_business, "blue", "Бизнес")
        self.buy_button = QPushButton("Купить")
        self.book_button = QPushButton("Забронировать")
        self.buy_button.clicked.connect(self.buy_seat)
        self.book_button.clicked.connect(self.book_seat)
        grid_layout.addWidget(self.buy_button)
        grid_layout.addWidget(self.book_button)
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(self.create_description_button_seat())
        self.setLayout(main_layout)

    def create_seat_buttons(self, layout, seats, color, seat_class):
        for seat_info in seats:
            seat_name = seat_info[0]
            button = QPushButton(seat_name)
            button.setCheckable(True)
            button.setObjectName(seat_name)
            button.clicked.connect(self.seat_selected)
            button.setStyleSheet(f"background-color: {color}; color: white")
            if self.is_seat_occupied(seat_name):
                button.setStyleSheet("background-color: black;")
                button.setEnabled(False)
            elif self.class_name != seat_class:
                button.setEnabled(False)
            layout.addWidget(button)

    @staticmethod
    def create_description_button_seat():
        description_button_seat = QHBoxLayout()
        economy_label = QLabel("Эконом-класс")
        economy_label.setStyleSheet("background-color: green; color: white; padding: 5px")
        description_button_seat.addWidget(economy_label)
        business_label = QLabel("Бизнес-класс")
        business_label.setStyleSheet("background-color: blue; color: white; padding: 5px")
        description_button_seat.addWidget(business_label)
        occupied_label = QLabel("Занято")
        occupied_label.setStyleSheet("background-color: black; color: white; padding: 5px")
        description_button_seat.addWidget(occupied_label)
        return description_button_seat

    def is_seat_occupied(self, seat_name):
        return (get_seat_book(self.from_, self.to_, self.date_, self.time_start, self.time_end, seat_name) or
                get_seat_buy(self.from_, self.to_, self.date_, self.time_start, self.time_end, seat_name))

    def seat_selected(self):
        sender = self.sender()
        self.seat_name = sender.objectName()
        if sender.isChecked():
            if self.selected_seat is not None:
                self.selected_seat.setChecked(False)
            self.selected_seat = sender
            print(f'Выбрано место: {self.seat_name}')
        else:
            self.selected_seat = None
            print(f"Убрано место: {self.seat_name}")

    def book_seat(self):
        if self.selected_seat is not None:
            seat_name = self.selected_seat.objectName()
            if not self.is_seat_occupied(seat_name):
                create_seat_book(self.id_, self.from_, self.to_, self.date_, seat_name)
                self.selected_seat.setEnabled(False)
                self.selected_seat = None
                print(f"Место {seat_name} успешно забронировано!")
                self.main_window_.add_info(seat_name)
                self.close()

    def buy_seat(self):
        if self.selected_seat is not None:
            seat_name = self.selected_seat.objectName()
            if not self.is_seat_occupied(seat_name):
                create_buy_ticket(self.id_, self.from_, self.to_, self.date_, seat_name)
                self.selected_seat.setEnabled(False)
                self.selected_seat = None
                print(f"Место {seat_name} успешно куплено!")
                self.main_window_.add_info_buy(seat_name)
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.exec_()
