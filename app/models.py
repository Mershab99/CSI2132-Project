from __future__ import annotations

import pynecone as pc
from sqlmodel import *
from datetime import date
from sqlalchemy_schemadisplay import create_schema_graph

import pcconfig


class Amenity(pc.Model, table=True):
    id: int = Field(primary_key=True)
    name: str


class Area(pc.Model, table=True):
    id: int = Field(primary_key=True)
    name: str


class RoomAmenity(pc.Model, table=True):
    room_id: int = Field(foreign_key="room.id", primary_key=True)
    amenity_id: int = Field(foreign_key="amenity.id", primary_key=True)


class HotelChain(pc.Model, table=True):
    id: int = Field(primary_key=True)
    name: str
    central_office_address: str
    email: str
    phone_number: str


class Hotel(pc.Model, table=True):
    id: int = Field(primary_key=True)
    hotel_chain_id: int = Field(foreign_key="hotelchain.id")
    name: str
    address: str
    area_id: int = Field(foreign_key="area.id")
    email: str
    phone_number: str


class Room(pc.Model, table=True):
    id: int = Field(primary_key=True)
    hotel_id: int = Field(foreign_key="hotel.id")
    number_of_rooms: int
    price: float
    capacity: int
    sea_view: bool
    mountain_view: bool
    extendable: bool
    problems: str


class People(pc.Model, table=True):
    id: int = Field(primary_key=True)
    full_name: str
    address: str
    ssn_sin: str
    registration_date: date
    email: str
    is_employee: bool


class EmployeeHotel(pc.Model, table=True):
    id: int = Field(primary_key=True)
    employee_id: int = Field(foreign_key="people.id")
    hotel_id: int = Field(foreign_key="hotel.id")


class Booking(pc.Model, table=True):
    id: int = Field(primary_key=True)
    customer_id: int = Field(foreign_key="people.id")
    room_id: int = Field(foreign_key="room.id")
    employee_id: int = Field(foreign_key="people.id")
    start_date: date
    end_date: date
    is_rented: bool


class Rental(pc.Model, table=True):
    id: int = Field(primary_key=True)
    customer_id: int = Field(foreign_key="people.id")
    room_id: int = Field(foreign_key="room.id")
    start_date: date
    end_date: str
    payment_amount: float


graph = create_schema_graph(metadata=MetaData(pcconfig.config.db_url),
                            show_datatypes=True, show_indexes=True)
graph.write_png('er_diagram.png')
