from API.salary import post_salary, put_salary, delete_salary
from managers.Show.Salary import salary_show


class SalaryModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def add_salary(self, input_line):
        amount = input_line[0].text()
        if amount:
            post_salary(amount)
            salary_show.show_data_salary(self.main_window)

    def update_salary(self, input_line):
        id_ = input_line[0].text()
        amount = input_line[1].text()
        if id_ and amount:
            put_salary(id_, amount)
            salary_show.show_data_salary(self.main_window)

    def delete_salary(self, input_line):
        id_ = input_line[0].text()
        if id_:
            delete_salary(id_)
            salary_show.show_data_salary(self.main_window)
