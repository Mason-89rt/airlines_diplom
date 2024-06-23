from fastapi import APIRouter
from endpoints.models import (StaffPhone, StaffNameSurname, Id, StaffSurname, StaffName, StaffSalary,
                              StaffGender,  StaffIDGenderUpdater, StaffIDSalaryUpdater, StaffNameUpdater,
                              StaffPhoneUpdater, StaffSurnameUpdater, StaffCreate, StaffInfo, StaffProfile,
                              StaffInfoUpdate)

from resolvers.staff import (get_staff, get_staff_phone, get_staff_id, delete_staff, post_staff,
                             get_staff_surname, get_staff_name, get_staff_id_gender, get_staff_id_salary,
                             get_staff_name_surname, get_phone, post_staff_id, put_staff_surname, put_staff_id_gender,
                             put_staff_phone, put_staff_id_salary, put_staff_name, get_staff_info, get_staff_profile,
                             put_staff_profile)

router = APIRouter()


@router.get('/staff/id')
def get_staff_endpoint(staff: Id):
    return get_staff_id(staff)


@router.put('/staff_info_update')
def get_staff_endpoint(endpoint: StaffInfoUpdate):
    return put_staff_profile(endpoint)


@router.get('/staff_info')
def get_staff_endpoint(endpoint: StaffInfo):
    return get_staff_info(endpoint)


@router.get('/staff_profile')
def get_staff_endpoint(endpoint: StaffProfile):
    return get_staff_profile(endpoint)


@router.get('/staffs')
def get_staff_endpoint():
    return get_staff()


@router.get('/staff_phone')
def get_staff_endpoint(staff: StaffPhone):
    return get_phone(staff)


@router.get('/staff/phone')
def get_staff_endpoint(staff: StaffPhone):
    return get_staff_phone(staff)


@router.post('/new_staff')
def new_staff(staff: StaffCreate):
    return post_staff(staff)


@router.get('/staff/name_surname')
def patch_staff_name(staff_update: StaffNameSurname):
    return get_staff_name_surname(staff_update)


@router.get('/staff/name')
def patch_staff_name(staff_update: StaffName):
    return get_staff_name(staff_update)


@router.get('/staff/surname')
def patch_staff_name(staff_update: StaffSurname):
    return get_staff_surname(staff_update)


@router.get('/staff/id_gender')
def patch_staff_name(staff_update: StaffGender):
    return get_staff_id_gender(staff_update)


@router.get('/staff/id_salary')
def patch_staff_name(staff_update: StaffSalary):
    return get_staff_id_salary(staff_update)


@router.post('/staff/new_id')
def post_staff_endpoint(staff: Id):
    return post_staff_id(staff)


@router.put('/staff/name')
def put_staff_endpoint(staff: StaffNameUpdater):
    return put_staff_name(staff)


@router.put('/staff/surname')
def put_staff_endpoint(staff: StaffSurnameUpdater):
    return put_staff_surname(staff)


@router.put('/staff/phone')
def put_staff_endpoint(staff: StaffPhoneUpdater):
    return put_staff_phone(staff)


@router.put('/staff/id_gender')
def put_staff_endpoint(staff: StaffIDGenderUpdater):
    return put_staff_id_gender(staff)


@router.put('/staff/id_salary')
def put_staff_endpoint(staff: StaffIDSalaryUpdater):
    return put_staff_id_salary(staff)


@router.delete('/staff/id')
def delete_staff_id(staff: Id):
    return delete_staff(staff)
