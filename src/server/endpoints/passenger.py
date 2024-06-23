from datetime import date


from fastapi import APIRouter
from endpoints.models import (PassengerDate, Passenger, PassengerNameSurname, PassengerId, Gender,
                              PassengerPersonalInfo, PassengerProfile, PassengerPersonalInfoUpdate,
                              UserdeleteID, PassengerPersonalInfoReg)
from resolvers.passenger import (get_passenger, get_passenger_gender, get_passenger_date, get_passenger_date_url,
                                 get_passenger_id, get_passenger_profile, get_profile, get_profile_register,
                                 get_name_surname_passenger, delete_passenger, put_passenger_profile,
                                 post_passenger_id, post_passenger_personal_info, post_passenger)
router = APIRouter()


@router.get('/passenger_profile')
def get_passenger_endpoint(endpoint: PassengerPersonalInfoUpdate):
    return get_passenger_profile(endpoint)


@router.get('/passenger_profile_text')
def get_passenger_endpoint(endpoint: PassengerProfile):
    return get_profile(endpoint)


@router.get('/passenger_profile_none')
def get_passenger_endpoint(endpoint: PassengerPersonalInfoReg):
    return get_profile_register(endpoint)


@router.put('/passenger_profile')
def get_passenger_endpoint(endpoint: PassengerPersonalInfoUpdate):
    return put_passenger_profile(endpoint)


@router.get('/passenger/id')
def get_passenger_endpoint(endpoint: PassengerId):
    return get_passenger_id(endpoint)


@router.get('/passenger/gender')
def get_passenger_gender_endpoint(endpoint: Gender):
    return get_passenger_gender(endpoint)


@router.get('/passenger/name')
def get_passenger_endpoint(endpoint: PassengerNameSurname):
    return get_name_surname_passenger(endpoint)


@router.get('/passenger/date')
def get_passenger_endpoint(endpoint: PassengerDate):
    return get_passenger_date(endpoint)


@router.get('/passenger/date/{date_birthday}')
def get_passenger_endpoint(endpoint: date):
    return get_passenger_date_url(endpoint)


@router.get('/passengers')
def get_passenger_endpoint():
    return get_passenger()


@router.post('/new_passenger')
def new_passenger(endpoint: Passenger):
    return post_passenger(endpoint)


@router.post('/new_personal_info')
def new_passenger(endpoint: PassengerPersonalInfo):
    return post_passenger_personal_info(endpoint)


@router.post('/new_id')
def new_passenger(endpoint: UserdeleteID):
    return post_passenger_id(endpoint)

# @router.put('/passenger_name/id')
# def patch_passenger_name(endpoint: PassengerNameSurname):
#     return put_passenger(endpoint)


@router.delete('/passenger/id')
def delete_passenger_id(endpoint: PassengerId):
    return delete_passenger(endpoint)
