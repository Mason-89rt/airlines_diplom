from PyQt5.QtWidgets import QApplication, QDialog
from generated.ticket_status_flight_ui import Ui_Form
import sys


class TicketStatusFlight(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = TicketStatusFlight()
    m.show()
    app.exec_()
