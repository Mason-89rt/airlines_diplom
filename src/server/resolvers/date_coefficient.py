from endpoints.models import DateCoefficient, DateCoefficientUpdater, DateSearch
from db.DBmanager import base_manager


def get_date_coefficient():
    res = base_manager.execute("select * from date_coefficient", args=())
    date_coefficient = []
    for i in res:
        date_coefficient.append(DateCoefficient(id=i[0], date_=i[1], coefficient=i[2]))
    return date_coefficient


def get_date_coefficient_():
    res = base_manager.execute("select date_, coefficient from date_coefficient", args=())
    date_coefficient = {}
    for i in res:
        date = i[0]
        coefficient = i[1]
        date_coefficient[date] = coefficient
    return date_coefficient


def get_date_coefficient_on_id(date_coefficient: DateSearch):
    res = base_manager.execute("select * from date_coefficient where date_=?", args=(date_coefficient.date_,))
    date_coefficient = []
    for i in res:
        date_coefficient.append(DateCoefficient(id=i[0], date_=i[1], coefficient=i[2]))
    return date_coefficient


def put_date_coefficient_on_id(date_coefficient: DateCoefficientUpdater):
    res = base_manager.execute("update date_coefficient set coefficient=? where id=?", args=(date_coefficient.
                                                                                             coefficient,
                                                                                             date_coefficient.id))
    return res
