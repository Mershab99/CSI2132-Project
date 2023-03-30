INSERT INTO hotelchain (name, central_office_address, email, phone_number) VALUES
('Hilton', '123 Main Street', 'hilton@example.com', '555-1234'),
('Marriott', '456 First Avenue', 'marriott@example.com', '555-5678'),
('InterContinental', '789 Fifth Street', 'intercontinental@example.com', '555-9012'),
('Accor', '321 Second Boulevard', 'accor@example.com', '555-3456'),
('Best Western', '654 Third Avenue', 'bestwestern@example.com', '555-7890');

INSERT INTO hotel (name, hotel_chain_id, address, email, phone_number) VALUES
('Hilton Hotel Downtown', 1, '100 Main St', 'downtown@hilton.com', '555-1000'),
('Hilton Hotel Uptown', 1, '200 Main St', 'uptown@hilton.com', '555-2000'),
('Hilton Hotel Midtown', 1, '300 Main St', 'midtown@hilton.com', '555-3000'),
('Marriott Hotel Downtown', 2, '100 First Ave', 'downtown@marriott.com', '555-4000'),
('Marriott Hotel Uptown', 2, '200 First Ave', 'uptown@marriott.com', '555-5000'),
('Marriott Hotel Midtown', 2, '300 First Ave', 'midtown@marriott.com', '555-6000'),
('InterContinental Hotel Downtown', 3, '100 Fifth St', 'downtown@intercontinental.com', '555-7000'),
('InterContinental Hotel Uptown', 3, '200 Fifth St', 'uptown@intercontinental.com', '555-8000'),
('InterContinental Hotel Midtown', 3, '300 Fifth St', 'midtown@intercontinental.com', '555-9000'),
('Novotel Hotel Downtown', 4, '100 Second Blvd', 'downtown@novotel.com', '555-1001'),
('Novotel Hotel Uptown', 4, '200 Second Blvd', 'uptown@novotel.com', '555-2001'),
('Novotel Hotel Midtown', 4, '300 Second Blvd', 'midtown@novotel.com', '555-3001'),
('Best Western Hotel Downtown', 5, '100 Third Ave', 'downtown@bestwestern.com', '555-4001'),
('Best Western Hotel Uptown', 5, '200 Third Ave', 'uptown@bestwestern.com', '555-5001'),
('Best Western Hotel Midtown', 5, '300 Third Ave', 'midtown@bestwestern.com', '555-6001');

INSERT INTO Room (number_of_rooms, price, amenities, capacity, sea_view, mountain_view, extendable, problems, hotel_id) VALUES
  (10, 150.00, '{wifi, air conditioning, tv}', 'double', true, false, true, '', 1),
  (5, 200.00, '{wifi, air conditioning, tv, minibar, balcony}', 'triple', true, false, true, '', 1),
  (8, 100.00, '{wifi, tv}', 'single', false, true, false, '', 1),
  (6, 300.00, '{wifi, air conditioning, tv, minibar, balcony}', 'suite', true, true, true, '', 1),
  (12, 100.00, '{wifi, tv}', 'single', true, false, false, '', 2),
  (7, 200.00, '{wifi, air conditioning, tv, minibar, balcony}', 'double', true, false, true, '', 2),
  (15, 150.00, '{wifi, air conditioning, tv}', 'twin', true, false, false, '', 2),
  (4, 250.00, '{wifi, air conditioning, tv, minibar, balcony}', 'suite', true, true, true, '', 3),
  (9, 120.00, '{wifi, tv}', 'single', false, true, false, '', 3),
  (6, 180.00, '{wifi, air conditioning, tv, balcony}', 'double', true, false, true, '', 3),
  (8, 80.00, '{wifi, tv}', 'single', true, false, false, '', 4),
  (11, 160.00, '{wifi, air conditioning, tv}', 'double', true, true, true, '', 4),
  (5, 250.00, '{wifi, air conditioning, tv, minibar, balcony}', 'suite', true, true, true, '', 4),
  (20, 200.00, '{wifi, air conditioning, tv}', 'double', false, true, false, '', 5),
  (13, 120.00, '{wifi, tv}', 'single', true, false, false, '', 5),
  (7, 180.00, '{wifi, air conditioning, tv, balcony}', 'double', true, true, true, '', 5);
