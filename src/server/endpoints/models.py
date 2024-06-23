from pydantic import BaseModel
from datetime import datetime, date, time
from typing import Optional


class StatusFlight(BaseModel):
    id_: int


class UserIdAndIdUser(BaseModel):
    id_: int
    id_user: int


class UserGetpassCreate(BaseModel):
    name: str


class UserGetpass(BaseModel):
    name: str


class UserState(BaseModel):
    user_id: int
    state: str


class UserStateCreate(BaseModel):
    user_id: int
    state: str


class UserUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None


class User(BaseModel):
    id: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None


class UserCreate(BaseModel):
    login: str
    password: str
    email: str
    role_id: int


class User_check(BaseModel):
    login: str
    password: str
    email: str


class UserIDLoginPasswordEmail(BaseModel):
    id: int
    login: str
    password: str
    email: str


class UserPassword(BaseModel):
    id: int
    password: str


class UserLoginPassword(BaseModel):
    login: str
    password: str


class UserLoginEmail(BaseModel):
    login: str
    email: str


class UserPasswordEmail(BaseModel):
    password: str
    email: str


class UserLoginPasswordEmail(BaseModel):
    login: str
    password: str
    email: str


class UserIDLoginPassword(BaseModel):
    id: int
    login: str
    password: str


class UserIDLoginEmail(BaseModel):
    id: int
    login: str
    email: str


class UserIDPasswordEmail(BaseModel):
    id: int
    password: str
    email: str


class UserPasswordID(BaseModel):
    password: str


class UserRole(BaseModel):
    id: int
    role_id: int


class UserRoleID(BaseModel):
    role_id: int


class UserdeleteID(BaseModel):
    id: Optional[int] = None


class UserEmail(BaseModel):
    id: int
    email: str


class UserEmailID(BaseModel):
    email: str


class UserLoginID(BaseModel):
    login: str


class UserLogin(BaseModel):
    id: int
    login: str


class UserID(BaseModel):
    login: str
    password: str
    email: str
    role_id: int
    id_: int


class Passenger(BaseModel):
    id: int
    name: str
    surname: str
    phone: str
    date_birthday: date
    address: str
    id_user: int
    id_gender: int


class PassengerProfile(BaseModel):
    id_: int


class PassengerPersonalInfo(BaseModel):
    name: str
    surname: str
    date_birthday: date
    phone: str
    id_user: int
    id_gender: int
    id_: int


class PassengerPersonalInfoReg(BaseModel):
    id_: int


class PassengerPersonalInfoUpdate(BaseModel):
    name: str
    surname: str
    date_birthday: date
    phone: str
    id_gender: int
    id_: int


class PassengerContact(BaseModel):
    phone: str


class PassengerDate(BaseModel):
    date_birthday: date


class PassengerId(BaseModel):
    id: int


class PassengerNameSurname(BaseModel):
    name: str
    surname: str


class Staff(BaseModel):
    id: int
    id_user: Optional[int] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    phone: Optional[str] = None
    date_birthday: Optional[date] = None
    id_gender: Optional[int] = None
    id_salary: Optional[int] = None


class StaffInfo(BaseModel):
    name: str
    surname: str
    phone: str
    date_birthday: date
    id_gender: int
    id: int


class StaffInfoUpdate(BaseModel):
    name: str
    surname: str
    phone: str
    date_birthday: Optional[date] = None
    id_gender: int
    id: int


class StaffProfile(BaseModel):
    id: int

class StaffCreate(BaseModel):
    name: str
    surname: str
    phone: str
    id_salary: int
    id_gender: int


class StaffNameSurname(BaseModel):
    name: str
    surname: str


class StaffName(BaseModel):
    name: str


class StaffNameUpdater(BaseModel):
    id: int
    name: str


class StaffSurnameUpdater(BaseModel):
    id: int
    surname: str


class StaffPhoneUpdater(BaseModel):
    id: int
    phone: str


class StaffIDGenderUpdater(BaseModel):
    id: int
    id_gender: int


class StaffIDSalaryUpdater(BaseModel):
    id: int
    id_salary: int


class StaffSurname(BaseModel):
    surname: str


class Id(BaseModel):
    id: int


class StaffPhone(BaseModel):
    phone: str


class StaffGender(BaseModel):
    gender: int


class StaffSalary(BaseModel):
    salary: int


class Role(BaseModel):
    id: int
    name: str


class RoleID(BaseModel):
    id: int


class RoleName(BaseModel):
    name: str


class ReviewStaff(BaseModel):
    id: int
    id_staff: int
    content: str


class ReviewStaffView(BaseModel):
    id: int
    id_staff: int
    content: str
    time_stamp: str


class ReviewTimestampStaff(BaseModel):
    time_stamp: datetime


class ReviewContentAndIdStaff(BaseModel):
    id_staff: int
    content: str


class ReviewPassenger(BaseModel):
    id: int
    id_passenger: int
    content: str


class ReviewPassengerView(BaseModel):
    id: int
    id_passenger: int
    content: str
    time_stamp: str


class ReviewTimestampPassenger(BaseModel):
    time_stamp: datetime


class ReviewContentAndIdPassenger(BaseModel):
    id_passenger: int
    content: str


class ResponseStaff(BaseModel):
    id: int
    id_response_staff: int
    id_receiving_passenger: int
    content: str


class ResponseViewStaff(BaseModel):
    id: int
    id_response_staff: int
    id_receiving_passenger: int
    content: str
    time_stamp: str


class ResponsePassenger(BaseModel):
    id: int
    id_response_passenger: int
    id_receiving_staff: int
    content: str


class ResponseViewPassenger(BaseModel):
    id: int
    id_response_passenger: int
    id_receiving_staff: int
    content: str
    time_stamp: str


class ResponseContent(BaseModel):
    id: int
    content: str


class ResponseTimestamp(BaseModel):
    time_stamp_response: str


class CompanyInformationView(BaseModel):
    id: int
    id_airline_company: int
    address: str
    web_site: str
    phone: str
    email: str
    rating: int
    date_of_creation: datetime


class CompanyPhoneEmail(BaseModel):
    id: int
    phone: str
    email: str


class CompanyWebSite(BaseModel):
    web_site: str


class CompanyNameRating(BaseModel):
    name: str
    rating: int


class Flights(BaseModel):
    id: int
    boarding: datetime
    id_route: int
    id_flights_status: int
    id_plane: int


class FlightsBoarding(BaseModel):
    boarding: int


class FlightsStatus(BaseModel):
    id: int
    from_flights: str
    to_flights: str
    date_departure: datetime


class FlightsStatusId(BaseModel):
    id: int


class Ticket(BaseModel):
    id: int
    seat: int
    id_class: int
    id_flights: int
    id_passenger: int


class TicketClass(BaseModel):
    id_class: int


class TicketSeat(BaseModel):
    seat: int


class TicketId(BaseModel):
    id: int


class Route(BaseModel):
    id: int
    id_directive: int
    id_directive_return: int
    date_route_start: date
    date_route_end: date
    time_start: time
    time_end: time


class DateFrom(BaseModel):
    date_from: date


class Route_time(BaseModel):
    time_start: time
    time_end: time


class RouteId(BaseModel):
    id: int


class Directive(BaseModel):
    from_directive: str
    to_directive: str
    date_: date


class DirectiveShow(BaseModel):
    id: int
    from_directive: str
    to_directive: str


class DirectiveFromTo(BaseModel):
    from_directive: str
    to_directive: str


class PlaneID(BaseModel):
    id: Optional[int] = None


class IDPlane(BaseModel):
    from_directive: str
    date_: date
    time_start: time
    time_end: time

class SeatBookID(BaseModel):
    id: int


class IDSeatBook(BaseModel):
    from_directive: str
    to_directive: str
    date_: date
    time_start: time
    time_end: time
    seat_name: str


class SeatBookCreate(BaseModel):
    id_passenger: int
    from_directive: str
    to_directive: str
    date_: date
    seat_name: str


class SeatBookDelete(BaseModel):
    passenger_id: int
    from_directive: str
    date_: date
    time_start: time
    time_end: time
    seat_name: str
    class_name: str


class SearchBookingTicketInfo(BaseModel):
    from_directive: str
    to_directive: str
    date_: date
    time_start: time
    time_end: time
    seat_name: str
    passenger_id: int


class SeatBookDeleteOnID(BaseModel):
    from_directive: str
    to_directive: str
    date_: date
    time_start: time
    time_end: time
    seat_name: str
    passenger_id: int


class FlightsCreate(BaseModel):
    flights_status: str
    from_directive: str
    to_directive: str
    time_start: time
    time_end: time
    date_: date
    plane_model: str
    gate: str


class FlightsShow(BaseModel):
    id_: int
    id_flights_status: int
    id_route: int
    id_time_: int
    id_date_: int
    id_plane: int
    id_gate: int


class FlightsUpdate(BaseModel):
    id_: int
    flights_status: str
    from_directive: str
    to_directive: str
    time_start: time
    time_end: time
    date_: date
    plane_model: str
    gate: str


class SeatBook(BaseModel):
    seat: Optional[str] = None


class BookCreate(BaseModel):
    from_directive: str
    date_: date
    time_start: time
    time_end: time
    class_name: str
    seat_name: str


class DirectiveFromUpdater(BaseModel):
    id: int
    from_directive: str


class DirectiveFrom(BaseModel):
    from_directive: str


class DirectiveTo(BaseModel):
    to_directive: str


class DirectiveToUpdater(BaseModel):
    id: int
    to_directive: str


class DirectiveId(BaseModel):
    id: int


class RegistrationOnFlights(BaseModel):
    id: int
    surname: str
    id_ticket: int


class RegistrationOnFlightsSurname(BaseModel):
    surname: str


class RegistrationOnFlightsIdTicket(BaseModel):
    id_ticket: int


class RegistrationOnFlightsId(BaseModel):
    id: int


class Payment(BaseModel):
    id: int
    amount: int
    payment_date: datetime
    status: str
    description: str
    currency: str
    id_passenger: int


class PaymentStatus(BaseModel):
    status: str
    description: str


class PaymentAmountCurrency(BaseModel):
    id: int
    amount: int
    currency: str


class PaymentDate(BaseModel):
    payment_date: datetime


class PaymentIdPassenger(BaseModel):
    id_passenger: int


class Class(BaseModel):
    id: int
    name: str


class ClassId(BaseModel):
    id: int


class ClassName(BaseModel):
    name: str


class ClassSubclass(BaseModel):
    subclass_id: int


class Subclass(BaseModel):
    id: int
    name: str
    id_class: int


class SubclassId(BaseModel):
    id: int


class SubclassName(BaseModel):
    name: str


class SubclassInfo(BaseModel):
    id: int
    description: str
    id_subclass: int


class SubclassInfoUpdater(BaseModel):
    id: int
    description: str


class SubclassPriceUpdater(BaseModel):
    id: int
    price: int


class SubclassPrice(BaseModel):
    id: int
    price: int
    id_subclass: int


class SubclassDescription(BaseModel):
    description: str


class Salary(BaseModel):
    id: int
    amount: int


class SalaryAmountUpdater(BaseModel):
    id: int
    amount: int


class SalaryAmountCreate(BaseModel):
    amount: int


class SalaryDelete(BaseModel):
    id: int


class Gender(BaseModel):
    id: int
    name: str


class GenderNameUpdater(BaseModel):
    id: int
    name: str


class GenderDelete(BaseModel):
    id: int


class DateCoefficient(BaseModel):
    id: int
    date_: date
    coefficient: float


class Coefficient(BaseModel):
    coefficient: float


class DateSearch(BaseModel):
    date_: date


class DateCoefficientUpdater(BaseModel):
    id: int
    coefficient: float


class AirlineCompany(BaseModel):
    id: int
    name: str


class Manufacturer(BaseModel):
    id: int
    name: str
    date_creation: date
    last_maintenance_date: date


class ManufacturerName(BaseModel):
    name: str


class ManufacturerLastMaintenance(BaseModel):
    last_maintenance_date: date


class Model(BaseModel):
    id: int
    name: str


class StatusPlane(BaseModel):
    id: int
    status: str


class RegistrationNumber(BaseModel):
    id: int
    number: int


class Plane(BaseModel):
    id: int
    count_seat: int
    count_passenger: int
    id_model: int
    id_registration_number: int
    id_status_plane: int
    id_manufacturer: int


class PlaneModel(BaseModel):
    id_model: int


class PlaneStatus(BaseModel):
    id_status_plane: int


class PlaneRegistrationNumber(BaseModel):
    id_registration_number: int


class PlaneManufacturer(BaseModel):
    id: int
    count_seat: int
    count_passenger: int
    id_model: int
    id_registration_number: int
    id_status_plane: int
    id_manufacturer: int


class PlaneSeat(BaseModel):
    count_seat: int
