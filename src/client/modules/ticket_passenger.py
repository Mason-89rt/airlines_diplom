from PyQt5.QtWidgets import QApplication, QDialog
from generated.ticket_passenger_ui import UiTicketPassenger
import sys


class TicketPassenger(QDialog, UiTicketPassenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = TicketPassenger()
    m.show()
    app.exec_()
