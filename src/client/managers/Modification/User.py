from API.user import (get_login_user, get_email_user, delete_user,
                             get_role_id_user, update_user_role, update_user_email, update_user_login,
                             update_user_password, get_password_user, get_user_on_id, get_id_login_user,
                             get_id_email_user, get_id_password_user, get_id_login_password_user,
                             get_id_login_email_user, get_id_password_email_user, get_id_login_password_email_user,
                             get_login_email_user, get_login_password_user, get_password_email_user,
                             get_login_password_email_user)
from PyQt5.QtWidgets import QMessageBox
from src.server.set import email_list_admin, email_list_intern, email_list_pilot, email_list_engineer
from managers.Show.User import user_show


class UserModification:
    def __init__(self, main_window):
        self.login = None
        self.id = None
        self.main_window = main_window

    def search_user(self, input_line):
        id_ = input_line[0].text()
        login = input_line[1].text()
        password = input_line[2].text()
        email = input_line[3].text()

        if id_ and login and password and email:
            sd = get_id_login_password_email_user(id_, login, password, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_login_password_email(self.main_window, id_, login, password, email)

        elif id_ and login and password:
            sd = get_id_login_password_user(id_, login, password)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_login_password(self.main_window, id_, login, password)

        elif login and password and email:
            sd = get_login_password_email_user(login, password, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_login_password_email(self.main_window, login, password, email)

        elif id_ and login and email:
            sd = get_id_login_email_user(id_, login, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_login_email(self.main_window, id_, login, password)

        elif id_ and password and email:
            sd = get_id_password_email_user(id_, password, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_password_email(self.main_window, id_, login, password)

        elif id_ and login:
            sd = get_id_login_user(id_, login)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_login(self.main_window, id_, login)

        elif id_ and password:
            sd = get_id_password_user(id_, login)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_password(self.main_window, id_, password)

        elif id_ and email:
            sd = get_id_email_user(id_, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_id_email(self.main_window, id_, email)

        elif login and password:
            sd = get_login_password_user(login, password)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_login_password(self.main_window, login, password)

        elif login and email:
            sd = get_login_email_user(login, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_login_email(self.main_window, login, email)

        elif password and email:
            sd = get_password_email_user(password, email)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_password_email(self.main_window, password, email)

        elif id_:
            s = get_user_on_id(id_)
            print(f'пользователь {s} найден')
            user_show.show_data_user_id(self.main_window, id_)

        elif login:
            sd = get_login_user(login)
            print(f'пользователь {sd} найден')
            user_show.show_data_user_login(self.main_window, login)

        elif password:
            sa = get_password_user(password)
            print(f'пользователь {sa} найден')
            user_show.show_data_user_password(self.main_window, password)

        elif email:
            sw = get_email_user(email)
            print(f'пользователь {sw} найден')
            user_show.show_data_user_email(self.main_window, email)

    @staticmethod
    def determine_role_id(email):
        if email in email_list_admin:
            return 1
        elif email in email_list_pilot:
            return 2
        elif email in email_list_engineer:
            return 3
        elif email in email_list_intern:
            return 4
        return 5

    # def add_record(self, input_line):
    #     fields_data = [input_field.text() for input_field in input_line]
    #     if all(fields_data):
    #         login, password, email = fields_data
    #         try:
    #             self.id = get_user_getpass_id(self.user)
    #             print(f"ID пользователя для обновления: {self.id}")
    #             update_user_getpass(self.id, login, password, email)
    #             role_id = self.determine_role_id(email)
    #             user_update_on_getpass_role_id(self.id, role_id)
    #             print("Пользователь зарегистрирован успешно!")
    #             if role_id == 1:
    #                 post_personal_staff_id(self.id)
    #             elif role_id == 5:
    #                 post_personal_id(self.id)
    #         except Exception as e:
    #             print(f"Ошибка регистрации: {e}")
    #     else:
    #         print("Введите логин, пароль и почту.")
    #     user_show.show_data_user(self.main_window)

    def edit_record(self, input_line):
        id_ = input_line[0].text()
        login = input_line[1].text()
        password = input_line[2].text()
        email = input_line[3].text()
        role_id = input_line[4].text()

        existing_user = get_login_user(login)
        existing_email = get_email_user(email)

        if existing_user:
            print("Пользователь с таким логином уже существует.")
        else:
            if id_ and login:
                update_login = update_user_login(id_, login)
                if update_login:
                    print("Логин обновлен")
                else:
                    print("Ошибка обновления логина")
                    return

        if existing_email:
            print("Пользователь с такой почтой уже существует.")
        else:
            if id_ and email:
                update_email = update_user_email(id_, email)
                if update_email:
                    print("Почта обновлена")
                else:
                    print("Ошибка обновления почты")
        if get_password_user(password):
            print("Пароль неизменен")
        else:
            if id_ and password:
                update_password = update_user_password(id_, password)
                if update_password:
                    print("Пароль обновлен")
                else:
                    print("Ошибка обновления пароля")
        if get_role_id_user(role_id):
            print("Роль неизменена")
        else:
            if id_ and role_id:
                update_role = update_user_role(id_, role_id)
                if update_role:
                    print("Роль обновлена")
                else:
                    print("Ошибка обновления роли")
        user_show.show_data_user(self.main_window)

    def delete_record(self, input_line):
        fields_data = [input_field.text() for input_field in input_line]
        if all(fields_data):
            id_ = int(fields_data[0])
            QMessageBox.information(None, "Информация",
                                    """Билет забронирован, вы можете его купить или отменить во вкладке `Мои рейсы`""")
            delete = delete_user(id_)
            if delete:
                print("Пользователь удален")
            else:
                print("Ошибка при удалении")
        else:
            print("Введите идентификатор пользователя который нужно удалить.")
        user_show.show_data_user(self.main_window)
