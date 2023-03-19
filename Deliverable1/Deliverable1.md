# CSI2132 E-Hotels Booking System Deliverable 1 Report
**Mershab Issadien** - *300027272*

## Database Schema
```
HotelChain (id PK, name UNIQUE, central_office_address, email, phone_number)

Hotel (id PK, name UNIQUE, hotel_chain_id FK HotelChain.id, address, email, phone_number)

Room (id PK, number_of_rooms, price, amenities, capacity, sea_view, mountain_view, extendable, problems, hotel_id FK Hotel.id)

Customer (id PK, full_name, address, ssn_sin, registration_date)

Employee (id PK, full_name, address, ssn_sin, role, hotel_id FK Hotel.id)

Booking (id PK, customer_id FK Customer.id, room_id FK Room.id, start_date, end_date, is_rented)

Renting (id PK, customer_id FK Customer.id, room_id FK Room.id, start_date, end_date, payment_amount)

```

This is a snippet from `app/models.py`.

Please Ignore the `pc.Model`. It is the Pynecone representation of SQLModel
```python

## DATABASE MODELS - CLASS REPRESENTATION

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
```

## ER Diagram
![ER Diagram](./er_diagram.png)



## Primary Key Constraints

The e-Hotels database schema includes the following tables, each with a primary key constraint:

- `HotelChain`: `id`
- `Hotel`: `id`
- `Room`: `id`
- `Employee`: `id`
- `Customer`: `id`
- `Booking`: `id`
- `Renting`: `id`

In each table, the primary key column is named `id`. These primary key constraints ensure that each row in a table is uniquely identified and can be referenced by other tables using foreign key constraints.

## Referential Integrity Constraints

In addition to primary key constraints, the e-Hotels database schema also includes several foreign key constraints to maintain referential integrity between tables:

- The `Hotel` table includes a foreign key to the `HotelChain` table, referencing the `id` column.
- The `Room` table includes a foreign key to the `Hotel` table, referencing the `id` column.
- The `Employee` table includes a foreign key to the `Hotel` table, referencing the `id` column, and a foreign key to the `HotelChain` table, referencing the `id` column.
- The `Booking` table includes a foreign key to the `Room` table, referencing the `id` column, and a foreign key to the `Customer` table, referencing the `id` column.
- The `Renting` table includes a foreign key to the `Booking` table, referencing the `id` column.

These foreign key constraints ensure that data in related tables is consistent and accurate. For example, a hotel cannot be deleted if it has associated rooms or employees, and a room cannot be deleted if it has associated bookings or rentings. By enforcing referential integrity, the e-Hotels database maintains the consistency and correctness of its data.

## Domain Constraints

- `hotelchain.name` is a `VARCHAR` of maximum length 100 characters.
- `hotelchain.email` is a `VARCHAR` of maximum length 100 characters and should match the format of an email.
- `hotelchain.phone_number` is a `VARCHAR` of maximum length 20 characters and should match the format of a phone number.
- `hotel.name` is a `VARCHAR` of maximum length 100 characters.
- `hotel.email` is a `VARCHAR` of maximum length 100 characters and should match the format of an email.
- `hotel.phone_number` is a `VARCHAR` of maximum length 20 characters and should match the format of a phone number.
- `room.price` is a `DECIMAL` value representing the cost of the room.
- `room.amenities` is a `VARCHAR` of maximum length 100 characters.
- `room.capacity` is a `VARCHAR` of maximum length 50 characters.
- `room.view` is a `VARCHAR` of maximum length 20 characters and should match the options `sea` or `mountain`.
- `room.extensible` is a `BOOLEAN` indicating whether the room can be extended with an additional bed or not.
- `customer.full_name` is a `VARCHAR` of maximum length 100 characters.
- `customer.address` is a `VARCHAR` of maximum length 200 characters.
- `customer.SSN` is a `VARCHAR` of exactly length 9 characters and should only contain digits.
- `employee.full_name` is a `VARCHAR` of maximum length 100 characters.
- `employee.address` is a `VARCHAR` of maximum length 200 characters.
- `employee.SSN` is a `VARCHAR` of exactly length 9 characters and should only contain digits.

## Track My Progress!

I'm Actively working on the project at the [Github Repo!](https://github.com/Mershab99/CSI2132-Project)
