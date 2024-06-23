create table role(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar
);
create table user(
id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
login varchar,
password varchar,
email varchar,
role_id integer,
id_user_name_system integer,
foreign key (id_user_name_system) references user_name_system(id)
foreign key (role_id) references role(id)
);
create table staff(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_user INTEGER,
name varchar,
surname varchar,
phone varchar,
date_birthday date,
id_gender integer,
id_salary integer,
foreign key (id_user) references user(id),
foreign key (id_gender) references gender(id),
foreign key (id_salary) references salary(id)
);
create table user_state(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_user INTEGER,
state varchar,
foreign key (id_user) references user(id)
);
create table user_name_system(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar
);
create table passenger(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar,
surname varchar,
phone varchar,
date_birthday date,
id_user INTEGER,
id_gender integer,
foreign key (id_user) references user(id),
foreign key (id_gender) references gender(id)
);
create table company_information(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name_company varchar,
address varchar,
web_site varchar,
phone varchar,
email varchar,
rating INTEGER,
date_of_creation date
);
create table flights(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_flights_status INTEGER NOT NULL,
id_route integer NOT NULL,
id_time_ integer NOT NULL,
id_date_ integer NOT NULL,
id_plane integer NOT NULL,
id_gate varchar NOT NULL,
foreign key (id_flights_status) references flights_status(id),
foreign key (id_date_) references date_route(id),
foreign key (id_time_) references time_route(id),
foreign key (id_route) references route(id),
foreign key (id_plane) references plane(id),
foreign key (id_gate) references gate(id)
);
create table flights_status(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
status varchar
);
create table bookings_ticket(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_passenger integer,
id_flights INTEGER,
id_seat integer,
foreign key (id_passenger) references passenger(id),
foreign key (id_flights) references flights(id),
foreign key (id_seat) references seat(id)
);
create table buy_ticket(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_passenger integer,
id_flights INTEGER,
id_seat integer,
foreign key (id_passenger) references passenger(id),
foreign key (id_flights) references flights(id),
foreign key (id_seat) references seat(id)
);
create table gender(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar
);
create table salary(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
amount integer
);
create table class(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar
);
create table subclass(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name varchar,
price integer,
description varchar,
id_class integer,
foreign key (id_class) references class(id)
);
create table directive(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
from_directive varchar,
to_directive varchar
);
create table route(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
id_directive int,
foreign key (id_directive) references directive(id)
);

create table manufacturer(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name integer,
date_manufacturer date,
last_maintenance_date date
);

create table model(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name integer,
count_seat integer,
id_manufacturer integer,
foreign key (id_manufacturer) references manufacturer(id)
);

create table registration_number(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
number integer
);

create table status_plane(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
status varchar
);

create table plane(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
count_passenger integer,
id_model integer,
id_registration_number integer,
id_status_plane integer,
foreign key (id_model) references model(id),
foreign key (id_registration_number) references registration_number(id),
foreign key (id_status_plane) references status_plane(id)
);

CREATE TABLE time_route(
    id integer PRIMARY KEY AUTOINCREMENT,
    time_start TIME NOT NULL,
    time_end TIME NOT NULL
);

CREATE TABLE date_route(
    id integer PRIMARY KEY AUTOINCREMENT,
    date_start DATE NULL
);

CREATE TABLE date_coefficient(
    id integer PRIMARY KEY AUTOINCREMENT,
    date_ DATE NULL,
    coefficient VARCHAR NULL
);

CREATE TABLE seat(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar,
    id_plane integer,
    id_class integer,
    foreign key (id_class) references class(id),
    foreign key (id_plane) references plane(id)
);

CREATE TABLE gate(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar
);
