from API.role import get_role


class RoleShow:
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_data_role(main_window):
        from TableHandler.TableDataHandler import TableDataHandler
        data = get_role()
        TableDataHandler.populate_table(main_window.table_role, data)


role_show = RoleShow()
