from datetime import datetime, timedelta
import datetime
from db.DBmanager import base_manager
from set import (routes, salaries, status_plane, registration_number, manufacturer, model, plane, company_information,
                 subclass, class_, role, flights, gender, route, seat, gate, status_flight, user_test, staff_test,
                 passenger_test, user_getpass_test, user_state)


class DataFiller:
    @staticmethod
    def calculate_and_insert_coefficients(start_date, end_date, min_coefficient=1.0, max_coefficient=5.0):
        total_days = (end_date - start_date).days
        current_date = start_date
        while current_date <= end_date:
            elapsed_days = (current_date - start_date).days
            # Calculate the coefficient as a fraction of the elapsed days, scaled to the min and max coefficients
            coefficient = min_coefficient + (max_coefficient - min_coefficient) * (elapsed_days / total_days)
            # Clamp the coefficient to the specified range
            coefficient = max(min_coefficient, min(max_coefficient, coefficient))
            # Format the date
            date_str = current_date.strftime('%Y-%m-%d')
            # Insert into the database
            base_manager.execute("INSERT INTO date_coefficient (date_, coefficient) VALUES (?, ?)",
                                 (date_str, coefficient))
            # Move to the next day
            current_date += timedelta(days=1)

    @staticmethod
    def fill_time_routes(start_hour=0, start_minute=0, hour_interval=0, minute_interval=0, num_records=0):
        start_time = datetime.datetime.strptime(f'{start_hour:02d}:{start_minute:02d}', '%H:%M')
        time_difference = timedelta(hours=hour_interval, minutes=minute_interval)
        for i in range(num_records):
            end_time = start_time + time_difference
            base_manager.execute("INSERT INTO time_route (time_start, time_end) "
                                 "VALUES (?, ?)",
                                 (start_time.strftime('%H:%M'), end_time.strftime('%H:%M')))
            start_time = end_time

    @staticmethod
    def fill_date_intervals(start_date):
        current_date = start_date
        for _ in range(365):
            base_manager.execute("INSERT INTO date_route (date_start) VALUES (?)",
                                 (current_date.strftime('%Y-%m-%d'),))
            current_date += timedelta(days=1)

    @staticmethod
    def fill_test_passenger():
        for data in passenger_test:
            base_manager.execute("INSERT INTO passenger (id_user) VALUES (?)", (data,))

    @staticmethod
    def fill_test_staff():
        for data in staff_test:
            base_manager.execute("INSERT INTO staff (id_user) VALUES (?)", (data,))

    @staticmethod
    def fill_test_user_getpass():
        for data in user_getpass_test:
            base_manager.execute("INSERT INTO user_name_system (name) VALUES (?)", (data,))

    @staticmethod
    def fill_test_user_state():
        for data in user_state:
            base_manager.execute("INSERT INTO user_state (id_user, state) VALUES (?, ?)", data,)

    @staticmethod
    def fill_test_user():
        for data in user_test:
            base_manager.execute("INSERT INTO user (login, password, email, role_id, id_user_name_system) "
                                 "VALUES (?, ?, ?, ?, ?)", data)

    @staticmethod
    def fill_routes():
        reverse_routes = [(to_, from_) for from_, to_ in routes]
        all_routes = routes + reverse_routes
        for from_, to_ in all_routes:
            base_manager.execute("INSERT INTO directive (from_directive, to_directive) VALUES (?, ?)", (from_, to_))

    @staticmethod
    def fill_salary():
        for salary in salaries:
            base_manager.execute("INSERT INTO salary (amount) VALUES (?)", (salary,))

    @staticmethod
    def fill_class_and_subclass():
        for data in class_:
            base_manager.execute("INSERT INTO class (name) VALUES (?)", data)
        for data in subclass:
            base_manager.execute("INSERT INTO subclass (name, price, description, id_class) VALUES (?, ?, ?, ?)", data)

    # @staticmethod
    # def fill_subclass_description():
    #     for data in subclass_description:
    #         base_manager.execute("INSERT INTO subclass_description (description, id_subclass) VALUES (?, ?)", data)
    #
    # @staticmethod
    # def fill_subclass_price():
    #     for data in subclass_price:
    #         base_manager.execute("INSERT INTO subclass_price (price, id_subclass) "
    #                              "VALUES (?, ?)", data)

    @staticmethod
    def fill_status_plane():
        for data in status_plane:
            base_manager.execute("INSERT INTO status_plane (status) VALUES (?)", (data,))

    # @staticmethod
    # def fill_registration_on_flights():
    #     for data in registration_on_flights:
    #         base_manager.execute("INSERT INTO registration_on_flights (surname, id_ticket) VALUES (?, ?)", data)

    @staticmethod
    def fill_registration_number():
        for data in registration_number:
            base_manager.execute("INSERT INTO registration_number (number) VALUES (?)", (data,))

    @staticmethod
    def fill_status_flight():
        for data in status_flight:
            base_manager.execute("INSERT INTO flights_status (status) VALUES (?)", (data,))

    @staticmethod
    def fill_manufacturer():
        for data in manufacturer:
            base_manager.execute("INSERT INTO manufacturer (name, date_manufacturer, last_maintenance_date) "
                                 "VALUES (?, ?, ?)", data)

    # @staticmethod
    # def fill_payment():
    #     for data in payment:
    #         base_manager.execute("INSERT INTO payment (amount, payment_date, status, "
    #                              "description, currency, id_passenger) "
    #                              "VALUES (?, ?, ?, ?, ?, ?)", data)

    @staticmethod
    def fill_company_information():
        for data in company_information:
            base_manager.execute("INSERT INTO company_information "
                                 "(name_company, address, web_site, phone, email, rating, date_of_creation) "
                                 "VALUES (?, ?, ?, ?, ?, ?, ?)", data)

    @staticmethod
    def fill_plane():
        for data in plane:
            base_manager.execute("INSERT INTO plane (count_passenger, id_model, "
                                 "id_registration_number, id_status_plane) "
                                 "VALUES (?, ?, ?, ?)", data)

    @staticmethod
    def fill_model():
        for data in model:
            base_manager.execute("INSERT INTO model (name, count_seat, id_manufacturer) VALUES (?, ?, ?)", data)

    @staticmethod
    def fill_route():
        for data in route:
            base_manager.execute("INSERT INTO route (id_directive) VALUES (?)", data)

    @staticmethod
    def fill_gender():
        for data in gender:
            base_manager.execute("INSERT INTO gender (name) VALUES (?)", (data,))

    # @staticmethod
    # def fill_airline_company():
    #     for data in airline_company:
    #         base_manager.execute("INSERT INTO airline_company (name) VALUES (?)", (data,))

    @staticmethod
    def fill_flights():
        for data in flights:
            base_manager.execute("INSERT INTO flights "
                                 "(id_flights_status, id_route, id_time_, id_date_, id_plane, id_gate) "
                                 "VALUES (?, ?, ?, ?, ?, ?)", data)

    @staticmethod
    def fill_role():
        for data in role:
            base_manager.execute("INSERT INTO role (name) VALUES (?)", (data,))

    @staticmethod
    def fill_seat():
        for data in seat:
            base_manager.execute("INSERT INTO seat (name, id_plane, id_class) VALUES (?, ?, ?)", data)

    @staticmethod
    def fill_gate():
        for data in gate:
            base_manager.execute("INSERT INTO gate (name) VALUES (?)", (data,))
