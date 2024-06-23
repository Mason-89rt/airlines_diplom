from API.user import (get_all_user, get_login_user, get_email_user, get_password_user, get_user_on_id,
                             get_id_login_user, get_id_email_user, get_id_password_user, get_id_login_password_user,
                             get_id_login_email_user, get_id_password_email_user, get_id_login_password_email_user,
                             get_login_email_user, get_login_password_user, get_password_email_user,
                             get_login_password_email_user)
from TableHandler.TableDataHandler import TableDataHandler


class UserShow:

    @staticmethod
    def show_data_user_login_password_email(main_window, login, password, email):
        data = get_login_password_email_user(login, password, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_login_password(main_window, login, password):
        data = get_login_password_user(login, password)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_password_email(main_window, password, email):
        data = get_password_email_user(password, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_login_email(main_window, login, email):
        data = get_login_email_user(login, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_login(main_window, id_, login):
        data = get_id_login_user(id_, login)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_password(main_window, id_, password):
        data = get_id_password_user(id_, password)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_email(main_window, id_, email):
        data = get_id_email_user(id_, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_login_password(main_window, id_, login, password):
        data = get_id_login_password_user(id_, login, password)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_login_email(main_window, id_, login, email):
        data = get_id_login_email_user(id_, login, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_password_email(main_window, id_, password, email):
        data = get_id_password_email_user(id_, password, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id_login_password_email(main_window, id_, login, password, email):
        data = get_id_login_password_email_user(id_, login, password, email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_password(main_window, password):
        data = get_password_user(password)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_login(main_window, login):
        data = get_login_user(login)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_email(main_window, email):
        data = get_email_user(email)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user_id(main_window, id_):
        data = get_user_on_id(id_)
        TableDataHandler.populate_table(main_window.table_user, data)

    @staticmethod
    def show_data_user(main_window):
        data = get_all_user()
        TableDataHandler.populate_table(main_window.table_user, data)


user_show = UserShow()
