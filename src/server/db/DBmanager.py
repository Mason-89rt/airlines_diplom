import sqlite3
from set import BASE_PATH, SCRIPTS_PATH
import os


class DBmanager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def cr_base(self, script_path: str):
        if not self.check_base():
            conn, cur = self.connect_base()
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_base()
        res = cur.execute(query, args)
        result = res.fetchall() if many else res.fetchone()
        conn.commit()
        return result

    def initialize(self):
        if not self.check_base():
            from db.DataFiller import DataFiller
            from datetime import datetime
            end_date = datetime(2024, 12, 31)
            start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
            self.cr_base(SCRIPTS_PATH)
            DataFiller.fill_time_routes(start_hour=0, start_minute=0, hour_interval=4, minute_interval=15,
                                        num_records=3)
            DataFiller.fill_date_intervals(start_date)
            DataFiller.fill_routes()
            DataFiller.fill_salary()
            DataFiller.fill_test_passenger()
            DataFiller.fill_test_user_getpass()
            DataFiller.fill_test_user()
            DataFiller.fill_test_staff()
            DataFiller.fill_class_and_subclass()
            DataFiller.calculate_and_insert_coefficients(start_date, end_date, min_coefficient=1.0, max_coefficient=4.0)
            DataFiller.fill_company_information()
            DataFiller.fill_test_user_state()
            DataFiller.fill_plane()
            DataFiller.fill_status_flight()
            DataFiller.fill_status_plane()
            DataFiller.fill_registration_number()
            DataFiller.fill_manufacturer()
            DataFiller.fill_model()
            DataFiller.fill_role()
            DataFiller.fill_route()
            DataFiller.fill_gender()
            DataFiller.fill_flights()
            DataFiller.fill_seat()
            DataFiller.fill_gate()


base_manager = DBmanager(BASE_PATH)
