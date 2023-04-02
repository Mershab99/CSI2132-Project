# CSI2132 E-Hotels Booking System Deliverable 1 Report
**Mershab Issadien** - *300027272*

## SQL Queries

### Table Creation
These are the table creation queries. Seperated are the Master tables and Application tables.

I have done this because in previous iterations I had each hotel with a list of amenities, this made it hard to create the booking form in which the customer may select any number of amenities
``` sql

-- Master Tables
CREATE TABLE Amenity(
    id INTEGER PRIMARY KEY,
    name VARCHAR 
)

CREATE TABLE Area(
    id INTEGER PRIMARY KEY,
    name VARCHAR 
)

-- Application Tables

CREATE TABLE RoomAmenity (
    room_id INTEGER REFERENCES Room(id),
    amenity_id INTEGER REFERENCES Amenity(id),
    PRIMARY KEY (room_id, amenity_id)
);

CREATE TABLE HotelChain (
    id INTEGER PRIMARY KEY,
    name VARCHAR UNIQUE,
    central_office_address VARCHAR,
    email VARCHAR,
    phone_number VARCHAR
);

CREATE TABLE Hotel (
    id INTEGER PRIMARY KEY,
    hotel_chain_id INTEGER REFERENCES HotelChain(id),
    name VARCHAR UNIQUE,
    address VARCHAR,
    area_id INTEGER REFERENCES Area(id)
    email VARCHAR,
    phone_number VARCHAR
);

CREATE TABLE Room (
    id INTEGER PRIMARY KEY,
    hotel_id INTEGER REFERENCES Hotel(id)
    number_of_rooms INTEGER,
    price FLOAT,
    capacity INTEGER,
    sea_view BOOLEAN,
    mountain_view BOOLEAN,
    extendable BOOLEAN,
    problems VARCHAR,
);

CREATE TABLE People (
    id INTEGER PRIMARY KEY,
    full_name VARCHAR,
    address VARCHAR,
    ssn_sin VARCHAR,
    registration_date DATE,
    email VARCHAR,
    is_employee BOOLEAN
);

CREATE TABLE EmployeeHotel (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER REFERENCES People(id),
    CONSTRAINT is_employee CHECK (
        employee_id IN (SELECT id FROM People WHERE is_employee = TRUE)
    ),
    hotel_id INTEGER REFERENCES Hotel(id)
);

CREATE TABLE Booking (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES People(id),
    room_id INTEGER REFERENCES Room(id),
    employee_id INTEGER REFERENCES People(id),
    start_date DATE,
    end_date DATE,
    is_rented BOOLEAN
);

CREATE TABLE Rental (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES Customer(id),
    room_id INTEGER REFERENCES Room(id),
    start_date DATE,
    end_date DATE,
    payment_amount FLOAT
);
```

### Indexes

I chose to create the following indexes as well:

1. `idx_people_email` This is to index the person's email, very useful as commonly people are looked up by email address and will provide performance improvements on actions like Login.
2. `idx_room_id` This is to index the RoomAmenity table by room_id because this table will be used for populating the list of amenities that fall under each Room (to select for booking).
3. `idx_room_customer_id` This index is to allow for performant lookup of a customer's bookings. As bookings will most likely be looked up by customer.

```sql
CREATE UNIQUE INDEX idx_people_email ON People(email)
CREATE UNIQUE INDEX idx_room_id ON RoomAmenity(room_id)
CREATE UNIQUE INDEX idx_room_customer_id ON Booking(customer_id)
```

### CRUD Operations

Provided below are sample CRUD (Create, Read, Update, Delete) operations for the application
#### Create
```sql
-- Create a new hotel chain
INSERT INTO HotelChain (name, central_office_address, email, phone_number) 
VALUES ('Hilton', '123 Main St', 'hilton@hilton.com', '555-555-5555');

-- Create a new hotel
INSERT INTO Hotel (hotel_chain_id, name, address, area_id, email, phone_number) 
VALUES (1, 'Hilton Toronto', '123 Yonge St', 1, 'toronto@hilton.com', '555-555-5555');

-- Create a new booking
INSERT INTO Booking (customer_id, room_id, employee_id, start_date, end_date, is_rented)
VALUES (1, 1, 1, '2023-04-01', '2023-04-07', TRUE);

-- Create a new rental
INSERT INTO Rental (customer_id, room_id, start_date, end_date, payment_amount)
VALUES (1, 1, '2023-04-08', '2023-04-15', 500);
```

#### Read
```sql
-- Get all hotels in a specific area
SELECT * FROM Hotel WHERE area_id = 1;

-- Get a specific booking by ID
SELECT * FROM Booking WHERE id = 1;

-- Get all rentals for a specific customer
SELECT * FROM Rental WHERE customer_id = 1;
```

#### Update
```sql
-- Update the phone number for a hotel
UPDATE Hotel SET phone_number = '555-123-4567' WHERE id = 1;

-- Update the end date for a booking
UPDATE Booking SET end_date = '2023-04-10' WHERE id = 1;

-- Update the payment amount for a rental
UPDATE Rental SET payment_amount = 600 WHERE id = 1;
```

#### Delete 
```sql
-- Delete a hotel chain and all associated hotels
DELETE FROM HotelChain WHERE id = 1;

-- Delete a booking
DELETE FROM Booking WHERE id = 1;

-- Delete a rental
DELETE FROM Rental WHERE id = 1;
```

### Triggers

This trigger will apply when a HotelChain entry is deleted. All the Hotels that belong to it are also deleted
```sql
-- Delete all Hotels that belong to a hotelchain
CREATE TRIGGER delete_hotels
AFTER DELETE ON HotelChain
FOR EACH ROW
BEGIN
    DELETE FROM Hotel WHERE hotel_chain_id = OLD.id;
END;
```
This trigger will apply when a Hotel entry is deleted. All the Rooms that belong to it are also deleted
```sql
CREATE TRIGGER delete_hotel_rooms
BEFORE DELETE ON Hotel
FOR EACH ROW
BEGIN
    DELETE FROM Room WHERE hotel_id = OLD.id;
END;
```

### Views


In this first view `AvailableRoomsPerArea`, We join Room, Hotel, and Area tables, using a `LEFT JOIN` on the Booking table to exclude rooms that are currently rented.
We then group by area, and sum the capacity of the available rooms, to get the total number of available rooms per area, the view has three columns: `area_id, area_name, available_rooms `
```sql
CREATE VIEW AvailableRoomsPerArea AS
SELECT Area.id AS area_id, Area.name AS area_name, SUM(Room.capacity) AS available_rooms
FROM Room
JOIN Hotel ON Room.hotel_id = Hotel.id
JOIN Area ON Hotel.area_id = Area.id
LEFT JOIN Booking ON Room.id = Booking.room_id AND Booking.is_rented = TRUE
WHERE Booking.id IS NULL
GROUP BY Area.id, Area.name;
```

In the second view `HotelRoomCapacity` we join Hotel and Room tables to get the name of the hotel, and the capacity of all the rooms associated with this hotel. Using the `SUM` function we aggregate the capacity values for each hotel, and use `GROUP BY` to group the results by hotel
It's usage is defined below, by passing in the desired hotel in leu of `specified_hotel` we can get the total room capacity of a specified hotel
```sql
CREATE VIEW HotelRoomCapacity AS
SELECT Hotel.name AS hotel_name, SUM(Room.capacity) AS total_capacity
FROM Hotel
JOIN Room ON Hotel.id = Room.hotel_id
GROUP BY Hotel.id;

-- Usage
SELECT * FROM HotelRoomCapacity WHERE hotel_name = 'specified_hotel';
```

### Dummy Data
```sql
-- Master Tables
INSERT INTO Amenity VALUES (1, 'WiFi');
INSERT INTO Amenity VALUES (2, 'Swimming pool');
INSERT INTO Amenity VALUES (3, 'Gym');
INSERT INTO Amenity VALUES (4, 'Spa');
INSERT INTO Amenity VALUES (5, 'Restaurant');
INSERT INTO Amenity VALUES (6, 'Bar');
INSERT INTO Amenity VALUES (7, 'Room service');

INSERT INTO Area VALUES (1, 'City center');
INSERT INTO Area VALUES (2, 'Beachfront');
INSERT INTO Area VALUES (3, 'Mountains');
INSERT INTO Area VALUES (4, 'Suburbs');

-- Hotel Chains
INSERT INTO HotelChain VALUES (1, 'Marriott', '123 Main St, New York, NY', 'info@marriott.com', '1-800-555-1234');
INSERT INTO HotelChain VALUES (2, 'Hilton', '456 Park Ave, Los Angeles, CA', 'info@hilton.com', '1-800-555-5678');
INSERT INTO HotelChain VALUES (3, 'InterContinental', '789 Fifth Ave, Chicago, IL', 'info@ihg.com', '1-800-555-9101');
INSERT INTO HotelChain VALUES (4, 'Accor', '321 Sixth St, Miami, FL', 'info@accor.com', '1-800-555-1213');
INSERT INTO HotelChain VALUES (5, 'Hyatt', '555 Seventh Ave, San Francisco, CA', 'info@hyatt.com', '1-800-555-1415');

-- Hotels
INSERT INTO Hotel VALUES (1, 1, 'Marriott Downtown', '123 Main St, New York, NY', 1, 'info@marriott.com', '1-212-555-1212');
INSERT INTO Hotel VALUES (2, 1, 'Marriott Midtown', '456 Park Ave, New York, NY', 1, 'info@marriott.com', '1-212-555-2323');
INSERT INTO Hotel VALUES (3, 1, 'Marriott Times Square', '789 Seventh Ave, New York, NY', 1, 'info@marriott.com', '1-212-555-3434');
INSERT INTO Hotel VALUES (4, 1, 'Marriott Long Island', '555 Fifth Ave, Long Island, NY', 2, 'info@marriott.com', '1-516-555-4545');
INSERT INTO Hotel VALUES (5, 2, 'Hilton Downtown', '111 W 6th St, Los Angeles, CA', 1, 'info@hilton.com', '1-213-555-5656');
INSERT INTO Hotel VALUES (6, 2, 'Hilton Beverly Hills', '9876 Wilshire Blvd, Beverly Hills, CA', 2, 'info@hilton.com', '1-310-555-6767');
INSERT INTO Hotel VALUES (7, 2, 'Hilton Santa Monica', '123 Ocean Ave, Santa Monica, CA', 2, 'info@hilton.com', '1-310-555-7878');
INSERT INTO Hotel VALUES (8, 2, 'Hilton Long Beach', '543 Seaside Way, Long Beach, CA', 3, 'info@hilton.com', '1-562-555-8989');
INSERT INTO Hotel VALUES (9, 3, 'InterContinental Magnificent Mile', '100 E Ontario St, Chicago, IL', 1, 'info@ihg.com', '1-312-555-909');
```
The programming languages used are Python (3.11) using the Pynecone framework. Which compiles the program into a NEXT.js application. It uses SQLLite as the database backend.

### Source Code
Source code is provided in `source.zip`, latest version can be found on GitHub link below
## Usage
In order to run the application, one simply has to: 
1. Clone the git repo:
`git clone https://github.com/Mershab99/CSI2132-Project.git`
OR unzip `source.zip`
2. Install Prerequisites:
     - Python 3.7+
     - NodeJS 12.22.0+
2. Run `pc run`
3. Navigate to `localhost:3000`

#### Enjoy!

### Notes

Between Deliverable 1 and 2 I adjusted the Database structure as implementing UI views became difficult (see Master amenities table above). Upon advice of a wonderful TA, I instead used Master tables for Area and Amenities, which allows for simplified UI implementation.
In addition, I combined the `Employee` and `Customer` tables, with the `is_employee` boolean as a signifier, and `EmployeeHotel` table to track the one-many relationship between Hotel and Employee with the constraint that the Person must be an employee (`is_employee = True` )

I was also advised to use Django instead of this experimental framework, in hind sight this would have been a much simpler endeavour, as I am primarily versed in Backend development, but due to time constraints I was unable to follow through.

# Thank you!