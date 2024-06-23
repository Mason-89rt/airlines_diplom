from endpoints.models import UserState, UserStateCreate, UserdeleteID
from db.DBmanager import base_manager


def get_user_state(user_state: UserdeleteID):
    res = base_manager.execute("select state from user_state where id_user=?", args=(user_state.id,))
    return res


def update_user_state(user_state: UserState):
    res = base_manager.execute("update user_state set state=? where id_user=?", args=(user_state.state,
                                                                                      user_state.user_id))
    return res


def insert_user_state(user_state: UserStateCreate):
    res = base_manager.execute("insert into user_state(id_user, state) VALUES(?, ?)", args=(user_state.user_id,
                                                                                            user_state.state,))
    return res