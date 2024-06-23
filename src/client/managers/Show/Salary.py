from API.salary import get_salary


class SalaryShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_salary(main_window):
        from TableHandler.TableDataHandler import TableDataHandler
        data = get_salary()
        TableDataHandler.populate_table(main_window.table_salary, data)


salary_show = SalaryShow()
