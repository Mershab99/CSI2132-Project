from __future__ import annotations
from typing import List, Optional, ForwardRef

import pynecone as pc
from sqlmodel import *
from sqlalchemy_schemadisplay import create_schema_graph

import pcconfig


class HotelChain(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=False)
    central_office_address: str
    email: str
    phone_number: str


class Hotel(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=False)
    hotel_chain_id: int = Field(foreign_key="hotelchain.id")
    address: str
    email: str
    phone_number: str


class Room(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number_of_rooms: int
    price: float
    amenities: List[str]
    capacity: str
    sea_view: bool
    mountain_view: bool
    extendable: bool
    problems: str
    hotel_id: int = Field(foreign_key="hotel.id")


class Customer(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    address: str
    ssn_sin: str
    registration_date: str


class Employee(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    address: str
    ssn_sin: str
    role: str
    hotel_id: int = Field(foreign_key="hotel.id")


class Booking(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    room_id: int = Field(foreign_key="room.id")
    start_date: str
    end_date: str
    is_rented: bool = False


class Renting(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    room_id: int = Field(foreign_key="room.id")
    start_date: str
    end_date: str
    payment_amount: float


# Define relationships after all classes have been created
HotelChain.hotels = Relationship(back_populates="hotel_chain")
Hotel.hotels = Relationship(back_populates="hotel_chain")
Hotel.hotel_chain = Relationship(back_populates="hotels")
Hotel.rooms = Relationship(back_populates="hotel")
Room.hotel = Relationship(back_populates="rooms")
Room.bookings = Relationship(back_populates="room")
Customer.bookings = Relationship(back_populates="customer")
Employee.hotel = Relationship(back_populates="employees")
Booking.customer = Relationship(back_populates="bookings")
Booking.room = Relationship(back_populates="bookings")
Renting.customer = Relationship(back_populates="rentings")
Renting.room = Relationship(back_populates="rentings")


graph = create_schema_graph(metadata=MetaData(pcconfig.config.db_url),
                            show_datatypes=True, show_indexes=True)
graph.write_png('er_diagram.png')
