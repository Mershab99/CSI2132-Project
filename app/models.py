from __future__ import annotations
from typing import List, Optional

import pynecone as pc
from sqlmodel import *
from sqlalchemy_schemadisplay import create_schema_graph

import pcconfig


class HotelChain(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    central_office_address: str
    email: str
    phone_number: str
    hotels: List['Hotel'] = Relationship(back_populates="hotel_chain")


class Hotel(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    hotel_chain_id: int = Field(foreign_key="hotelchain.id")
    address: str
    email: str
    phone_number: str
    hotel_chain: Optional[HotelChain] = Relationship(back_populates="hotels")
    rooms: List[Room] = Relationship(back_populates="hotel")


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
    hotel: Optional[Hotel] = Relationship(back_populates="rooms")
    bookings: List[Booking] = Relationship(back_populates="room")


class Customer(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    address: str
    ssn_sin: str
    registration_date: str
    bookings: List[Booking] = Relationship(back_populates="customer")


class Employee(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    address: str
    ssn_sin: str
    role: str
    hotel_id: int = Field(foreign_key="hotel.id")
    hotel: Optional[Hotel] = Relationship(back_populates="employees")


class Booking(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Optional[Customer] = Relationship(back_populates="bookings")
    room_id: int = Field(foreign_key="room.id")
    room: Optional[Room] = Relationship(back_populates="bookings")
    start_date: str
    end_date: str
    is_rented: bool = False


class Renting(pc.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Optional[Customer] = Relationship(back_populates="rentings")
    room_id: int = Field(foreign_key="room.id")
    room: Optional[Room] = Relationship(back_populates="rentings")
    start_date: str
    end_date: str
    payment_amount: float


#graph = create_schema_graph(metadata=MetaData(pcconfig.config.db_url),
#                            show_datatypes=True, show_indexes=True)
#graph.write_png('er_diagram.png')
