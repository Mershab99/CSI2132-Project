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
INSERT INTO Hotel VALUES (9, 3, 'InterContinental Magnificent Mile', '100 E Ontario St, Chicago, IL', 1, 'info@ihg.com', '1-312-555-909
