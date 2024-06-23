from endpoints.models import (Staff, StaffPhone, StaffNameSurname, Id, StaffSurname, StaffName, StaffSalary,
                              StaffGender, StaffIDGenderUpdater, StaffIDSalaryUpdater, StaffNameUpdater,
                              StaffPhoneUpdater, StaffSurnameUpdater, StaffCreate, StaffInfo, StaffProfile,
                              StaffInfoUpdate)
from db.DBmanager import base_manager


def get_staff_id(staff: Id):
    res = base_manager.execute("SELECT * FROM staff WHERE id=?", args=(staff.id,), many=True)
    staff = []
    for i in res:
        staff.append(Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5],
                           id_gender=i[6], id_salary=i[7]))
    return staff


def get_staff_profile(staff: StaffProfile):
    res = base_manager.execute("""select name, surname, phone, date_birthday, id_gender, id_salary from staff where 
    id_user=?""", args=(staff.id,), many=False)
    return res


def put_staff_profile(staff: StaffInfoUpdate):
    res = base_manager.execute("""UPDATE staff SET 
    name = ?, 
    surname = ?, 
    phone = ?, 
    date_birthday = ?, 
    id_gender = ?
WHERE 
    id_user = ? 
    """, args=(staff.name, staff.surname, staff.phone, staff.date_birthday, staff.id_gender, staff.id))
    return res


def get_staff_info(staff: StaffInfo):
    res = base_manager.execute("""select name, surname, phone, date_birthday, id_gender, id_salary from staff where 
    name=? and surname=? and phone=? and date_birthday=? and id_gender=? and id_user=?""",
                               args=(staff.name, staff.surname, staff.phone, staff.date_birthday, staff.id_gender,
                                     staff.id), many=False)
    return res


def get_staff():
    res = base_manager.execute("select * from staff", args=(), many=True)
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def get_staff_phone(staff: StaffPhone):
    res = base_manager.execute("select * from staff where phone=?", args=(staff.phone,))
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def post_staff_id(staff: Id):
    res = base_manager.execute("""insert into staff(id_user) select id from user where id=?""",
                               args=(staff.id,))
    return res


def get_phone(staff: StaffPhone):
    res = base_manager.execute("select phone from staff where phone=?", args=(staff.phone,))
    return res


def get_staff_name_surname(staff: StaffNameSurname):
    res = base_manager.execute("select * from staff where name = ? and surname = ?", args=(staff.name, staff.surname))
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def get_staff_name(staff: StaffName):
    res = base_manager.execute("select * from staff where name=?", args=(staff.name,))
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def get_staff_surname(staff: StaffSurname):
    res = base_manager.execute("select * from staff where surname=?", args=(staff.surname,))
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def get_staff_id_gender(staff: StaffGender):
    res = base_manager.execute("select * from staff where id_gender=?", args=(staff.gender,))
    staff = []
    for i in res:
        staff.append(Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5],
                           id_gender=i[6], id_salary=i[7]))
    return staff


def get_staff_id_salary(staff: StaffSalary):
    res = base_manager.execute("select * from staff where id_salary=?", args=(staff.salary,))
    staff = []
    for i in res:
        staff.append(
            Staff(id=i[0], id_user=i[1], name=i[2], surname=i[3], phone=i[4], date_birthday=i[5], id_gender=i[6],
                  id_salary=i[7]))
    return staff


def post_staff(staff: StaffCreate):
    res = base_manager.execute("insert into staff(name,surname,phone, id_gender, id_salary) values(?,?,?,?,?)",
                               args=(staff.name, staff.surname, staff.phone, staff.id_gender,
                                     staff.id_salary))
    return res


def put_staff(staff_update: StaffNameSurname):
    res = base_manager.execute("update staff set name=?, surname=? where id=?",
                               args=(staff_update.name, staff_update.surname, staff_update.id))
    return res


def put_staff_name(staff_update: StaffNameUpdater):
    res = base_manager.execute("update staff set name=? where id=?",
                               args=(staff_update.name, staff_update.id))
    return res


def put_staff_surname(staff_update: StaffSurnameUpdater):
    res = base_manager.execute("update staff set surname=? where id=?",
                               args=(staff_update.surname, staff_update.id))
    return res


def put_staff_phone(staff_update: StaffPhoneUpdater):
    res = base_manager.execute("update staff set phone=? where id=?",
                               args=(staff_update.phone, staff_update.id))
    return res


def put_staff_id_gender(staff_update: StaffIDGenderUpdater):
    res = base_manager.execute("update staff set id_gender=? where id=?",
                               args=(staff_update.id_gender, staff_update.id))
    return res


def put_staff_id_salary(staff_update: StaffIDSalaryUpdater):
    res = base_manager.execute("update staff set id_salary=? where id=?",
                               args=(staff_update.id_salary, staff_update.id))
    return res


def delete_staff(staff: Id):
    res = base_manager.execute("delete from staff where id=?", args=(staff.id,))
    return res
