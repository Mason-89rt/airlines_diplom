from client.API.role import post_role, put_role, delete_role
from managers.Show.Role import role_show


class RoleModification:
    def __init__(self, main_window):
        self.main_window = main_window

    def add_role(self, input_line):
        name = input_line[0].text()
        if name:
            post_role(name)
            role_show.show_data_role(self.main_window)

    def update_role(self, input_line):
        id_ = input_line[0].text()
        name = input_line[1].text()
        if id_ and name:
            put_role(id_, name)
            role_show.show_data_role(self.main_window)

    def delete_role(self, input_line):
        id_ = input_line[0].text()
        if id_:
            delete_role(id_)
            role_show.show_data_role(self.main_window)
