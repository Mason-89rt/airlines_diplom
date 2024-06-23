from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression
from generated.login_form_ui import Ui_Dialog
from API.user import (update_user_getpass, get_id_user, check_user, get_email, post_user_none,
                      user_update_on_getpass_role_id, get_login_user)
from API.user_getpass import post_user_getpass, get_user_getpass_name, get_user_getpass_id
from API.passenger import post_personal_id
from API.staff import post_personal_staff_id
from API.user_state import get_user_state, update_user_state, insert_user_state
import sys
import os
print(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.server.set import email_list_admin, email_list_intern, email_list_pilot, email_list_engineer
from modules.main_window import MainWindow
from modules.main_window_user import MainWindowUser
import getpass
import re




class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.main_window_user = None
        self.main_window = None
        self.setupUi(self)
        self.id = None
        self.state_yes = 'Yes'
        self.user = getpass.getuser()
        self.setWindowTitle("Аутентификация")
        self.btn_sign_up.clicked.connect(self.btn_up)
        self.btn_sign_in.clicked.connect(self.btn_in)
        self.btn_up()
        self.check_state()

        email_regex = QRegularExpression(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_validator = QRegularExpressionValidator(email_regex, self.line_email)
        self.line_email.setValidator(email_validator)

    @staticmethod
    def determine_role_id(email):
        print(f"Определяем роль для email: {email}")
        if email in email_list_admin:
            return 1
        elif email in email_list_pilot:
            return 2
        elif email in email_list_engineer:
            return 3
        elif email in email_list_intern:
            return 4
        return 5

    def check_state(self):
        self.id = get_user_getpass_id(self.user)
        if self.id is None:
            post_user_getpass(self.user)
            self.id = post_user_none(self.user)
            self.id = get_user_getpass_id(self.user)
            print('Пользователь создан с ID:', self.id)

            if self.id is not None:
                insert_user_state(self.id, 'No')
                print('State создан')

        state = get_user_state(self.id)

        if self.id is not None and state:
            current_state = state[0][0]
            if current_state == 'Yes':
                self.process_active_user()
            elif current_state == 'No':
                self.show()

    def process_active_user(self):
        user_name = get_user_getpass_name(self.user)
        email = get_email(self.id)

        if user_name is not None and email[0] is not None:
            print(f"Получен email: {email[0]}")
            role_id = self.determine_role_id(email[0])
            print(f"Role ID: {role_id}, Email: {email[0]}")
            if role_id is not None:
                self.open_main_window(role_id)
                self.close()

    def btn_in(self):
        self.btn_sign_in.setStyleSheet("""
            QPushButton {
               color: #0043D4;
               background-color: rgb(255, 255, 255);
               border-bottom: 3px solid #0043D4;
            }
        """)
        self.btn_sign_up.setStyleSheet("")
        self.btn_sign_up.setChecked(False)
        self.btn_Log_In.setText("Войти")

        try:
            self.btn_Log_In.clicked.disconnect(self.register)
        except TypeError:
            pass
        self.btn_Log_In.clicked.connect(self.enter)

    def btn_up(self):
        self.btn_sign_up.setStyleSheet("""
            QPushButton {
                color: #0043D4;
               background-color: rgb(255, 255, 255);
               border-bottom: 3px solid #0043D4;
            }
        """)
        self.btn_sign_in.setStyleSheet("")
        self.btn_sign_in.setChecked(False)
        self.btn_Log_In.setText("Зарегистрироваться")
        try:
            self.btn_Log_In.clicked.disconnect(self.enter)
        except TypeError:
            pass
        self.btn_Log_In.clicked.connect(self.register)

    def register(self):
        login = self.line_login.text()
        password = self.line_password.text()
        email = self.line_email.text()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not login or not password or not email:
            QMessageBox.warning(self, "info", "Введите логин, пароль и почту в формате example@example.com")
            return

        if not re.match(email_pattern, email):
            QMessageBox.warning(self, "info", "Введите почту в формате example@example.com")
            return

        if len(password) < 6:
            QMessageBox.warning(self, "info", "Введите пароль более 6 символов")
            return

        try:
            existing_login = get_login_user(login)

            if existing_login:
                QMessageBox.warning(self, "info", "Пользователь с таким логином существует")
                return

            if get_email(self.id) is not None:
                QMessageBox.warning(self, "info", "Вы уже зарегистрированы")
                return

            print(f"ID пользователя для обновления: {self.id}")
            update_user_getpass(self.id, login, password, email)

            role_id = self.determine_role_id(email)
            user_update_on_getpass_role_id(self.id, role_id)
            update_user_state(self.id, self.state_yes)

            print("Пользователь зарегистрирован успешно!")

            if role_id == 1:
                post_personal_staff_id(self.id)
            elif role_id == 5:
                post_personal_id(self.id)

            self.open_main_window(role_id)

        except Exception as e:
            print(f"Ошибка регистрации: {e}")
            QMessageBox.warning(self, "info", f"Ошибка регистрации: {e}")

    def open_main_window(self, role_id):
        if role_id == 1:
            self.main_window = MainWindow(self.id)
            self.main_window.clear_data_profile()
            self.main_window.fill_data_profile()
            self.main_window.show()
        elif role_id == 5:
            self.main_window_user = MainWindowUser(self.id)
            self.main_window_user.clear_data_profile()
            self.main_window_user.fill_data_profile()
            self.main_window_user.fill_data_tickets()
            self.main_window_user.show()
        self.close()

    def enter(self):
        login = self.line_login.text()
        password = self.line_password.text()
        email = self.line_email.text()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if login and password and re.match(email_pattern, email):
            try:
                success = check_user(login, password, email)
                if success:
                    role_id_select = self.determine_role_id(email)
                    self.id = get_id_user(login)
                    update_user_state(self.id, self.state_yes)
                    print(f"ID пользователя при входе: {self.id}")
                    self.open_main_window(role_id_select)
                else:
                    QMessageBox.warning(self, "info", "Данные введены неверно.")
            except Exception as e:
                print(f"Ошибка при входе: {e}")
        else:
            QMessageBox.warning(self, "info", "Введите логин, пароль и почту в формате example@example.com")


if __name__ == "__main__":
    app = QApplication([])
    dialog = MyDialog()
    app.exec_()
