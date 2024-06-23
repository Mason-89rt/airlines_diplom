from PyQt5.QtWidgets import QApplication, QDialog
from generated.ticket_my_flights_ui import Ui_Ticket_My_Flights
import sys


class TicketMyFlights(QDialog, Ui_Ticket_My_Flights):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = TicketMyFlights()
    m.show()
    app.exec_()
