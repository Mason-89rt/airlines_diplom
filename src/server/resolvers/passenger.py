from datetime import date


from fastapi import APIRouter
from endpoints.models import (PassengerDate, Passenger, PassengerNameSurname, PassengerId, Gender,
                              PassengerPersonalInfo, PassengerProfile, PassengerPersonalInfoUpdate,
                              UserdeleteID, PassengerPersonalInfoReg, UserIdAndIdUser)
from db.DBmanager import base_manager
router = APIRouter()


def get_passenger_profile(passenger: PassengerPersonalInfoUpdate):
    res = base_manager.execute("""SELECT passenger.name, passenger.surname, passenger.date_birthday, 
    passenger.phone, id_gender from passenger
    where passenger.name=? and passenger.surname=? and passenger.date_birthday=? and
     passenger.phone=? and passenger.id_gender=? and id_user=?""", args=(passenger.name, passenger.surname,
                                                                         passenger.date_birthday, passenger.phone,
                                                                         passenger.id_gender, passenger.id_),
                               many=False)
    return res


def get_profile(passenger: PassengerProfile):
    res = base_manager.execute("""SELECT passenger.name, passenger.surname, passenger.date_birthday, 
    passenger.phone, id_gender from passenger
    where id_user=?""", args=(passenger.id_,), many=False)
    return res


def get_profile_register(passenger: PassengerPersonalInfoReg):
    res = base_manager.execute("""SELECT passenger.name, passenger.surname, passenger.date_birthday, 
    passenger.phone, id_gender from passenger
    where id_user=?""", args=(passenger.id_,), many=False)
    return res


def put_passenger_profile(passenger: PassengerPersonalInfoUpdate):
    res = base_manager.execute("""UPDATE passenger SET 
    name = ?, 
    surname = ?, 
    date_birthday = ?, 
    phone = ?, 
    id_gender = ?
WHERE 
    id_user = ? 
    """, args=(passenger.name, passenger.surname, passenger.date_birthday, passenger.phone, passenger.id_gender,
               passenger.id_))
    return res

# def put_passenger_id_user(passenger: UserIdAndIdUser):
#     res = base_manager.execute("""UPDATE passenger SET
#     id_user = ? select id_user from user where id=?
#     """, args=(passenger.id_user, passenger.id_))
#     return res

def get_passenger_id(passenger: PassengerId):
    row = base_manager.execute("SELECT * FROM passenger WHERE id=?", args=(passenger.id,), many=False)
    return Passenger(id=row[0], name=row[1], surname=row[2], phone=row[3], date_birthday=row[4],
                     address=row[5], id_user=row[6], id_gender=row[7])


def get_name_surname_passenger(passenger: PassengerNameSurname):
    res = base_manager.execute("SELECT * FROM passenger WHERE name=? and surname=?",
                               args=(passenger.name, passenger.surname), many=True)
    if res:
        passengers = [PassengerNameSurname(id=row[0], name=row[1], surname=row[2], phone=row[3], date_birthday=row[4],
                                           address=row[5], id_user=row[6]) for row in res]
        return passengers
    else:
        return None


def get_passenger_gender(gender: Gender):
    row = base_manager.execute("SELECT passenger.id,passenger.name,surname,date_birthday,"
                               "phone,address,id_user, gender.name "
                               "AS gender_name FROM passenger "
                               "INNER JOIN gender ON passenger.id_gender = gender.id where gender.id=?",
                               args=(gender.id,), many=True)
    return row


def get_passenger_date(date_birthday: PassengerDate):
    res = base_manager.execute("SELECT * FROM passenger WHERE date_birthday=?", args=(date_birthday.date_birthday,))
    if res:
        passengers = [Passenger(id=row[0], name=row[1], surname=row[2], phone=row[3], date_birthday=row[4],
                                address=row[5], id_user=row[6]) for row in res]
        return passengers
    else:
        return None


def get_passenger_date_url(date_birthday: date):
    res = base_manager.execute("SELECT * FROM passenger WHERE date_birthday=?", args=(date_birthday,))
    if res:
        passengers = [Passenger(id=row[0], name=row[1], surname=row[2], phone=row[3], date_birthday=row[4],
                                address=row[5], id_user=row[6]) for row in res]
        return passengers
    else:
        return None


def get_passenger():
    res = base_manager.execute("select * from passenger", args=(), many=True)
    passengers = []
    for row in res:
        passengers.append(Passenger(id=row[0], name=row[1], surname=row[2], phone=row[3], date_birthday=row[4],
                                    address=row[5], id_user=row[6], id_gender=row[7]))
    return passengers


def post_passenger(passenger: Passenger):
    res = base_manager.execute("insert into passenger(id,name,surname,phone,address,id_user,id_gender) "
                               "values(?,?,?,?,?,?,?)", args=(passenger.id, passenger.name, passenger.surname,
                                                              passenger.phone, passenger.address, passenger.id_user,
                                                              passenger.id_gender))
    return res


def post_passenger_personal_info(passenger: PassengerPersonalInfo):
    id_user = passenger.id_
    res = base_manager.execute("""INSERT INTO passenger (id_user) 
    SELECT ? from user WHERE id = ?;""", args=(id_user,))
    return res


def post_passenger_id(passenger: UserdeleteID):
    res = base_manager.execute("""insert into passenger(id_user) select id from user where id=?""",
                               args=(passenger.id,))
    return res


def put_passenger(id: int, passenger_update: PassengerNameSurname):
    res = base_manager.execute("update passenger set name=?, surname=? where id=?", args=(passenger_update.name,
                                                                                          passenger_update.surname, id))
    return res


def delete_passenger(passenger: PassengerId):
    res = base_manager.execute("delete from passenger where id=?", args=(passenger.id,))
    return res
