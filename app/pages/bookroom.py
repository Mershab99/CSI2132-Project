"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging

from app.basestate import BaseState, DUMMY_DATA
from app.models import *

logger = logging.getLogger(__name__)

room_columns = ["number of rooms", "price", "amenities", "capacity"]
start_date: str = "2023-04-03"
end_date: str = "2023-04-05"
capacity: int = 4


def get_amenities():
    if not DUMMY_DATA:
        with pc.session() as session:
            # create a raw SQL query using SQLAlchemy's text() function
            query = text("""
                    WITH RECURSIVE split_amenities AS (
                        SELECT amenities, 0 AS start_pos, NULL AS end_pos
                        FROM room
                        UNION ALL
                        SELECT amenities, end_pos + 1, INSTR(SUBSTR(amenities, end_pos + 1), ',')
                        FROM split_amenities
                        WHERE end_pos IS NOT NULL
                    )
                    SELECT DISTINCT TRIM(SUBSTR(amenities, start_pos, COALESCE(end_pos, LENGTH(amenities) + 1) - start_pos)) AS amenity
                    FROM split_amenities
                    WHERE TRIM(SUBSTR(amenities, start_pos, COALESCE(end_pos, LENGTH(amenities) + 1) - start_pos)) != '';
                """)
            result = session.execute(query)
            amenities = [row['amenity'] for row in result]
            amenities_set = set()

            for amenities_string in amenities:
                # remove the curly braces and split the string by commas
                amenities = amenities_string.strip('{}').split(',')

                # add each amenity to the set
                for amenity in amenities:
                    amenities_set.add(amenity.strip())

            # convert the set back to a list and sort it
            amenities_combined = sorted(list(amenities_set))
            return amenities_combined
    else:
        return []


def get_available_rooms():
    if not DUMMY_DATA:
        with pc.session() as session:
            query = """
            SELECT number_of_rooms, price, amenities, capacity FROM room
            WHERE capacity = :specified_capacity
            AND id NOT IN (
            SELECT room_id FROM renting
            WHERE (start_date <= :end_date AND end_date >= :end_date)
            OR (start_date <= :start_date AND end_date >= :start_date)
            OR (start_date >= :start_date AND end_date <= :end_date)
            )
            """
            params = {
                'start_date': start_date,
                'end_date': end_date,
                'specified_capacity': capacity
            }
            result = session.execute(query, params)
            # Extract only JSON-serializable data types from each row
            rows = [[str(cell) for cell in row if isinstance(cell, (str, int, float))] for row in result]
            print(rows)
            return rows

    else:
        return []


class SearchState(BaseState):
    start_date: str = ""
    end_date: str = ""
    capacity: int = 0

    def set_start_date(self, text):
        self.start_date = text

    def set_end_date(self, text):
        self.start_date = text

    def set_capacity(self, value):
        self.capacity = value

    def make_booking(self):
        if not DUMMY_DATA:
            with pc.session() as session:
                query = """
                    INSERT INTO Booking (customer_id, room_id, start_date, end_date, is_rented)
                    VALUES (:customer_id, :room_id, :start_date, :end_date, :is_rented)
                """
                params = {
                    'customer_id': 1,
                    'room_id': 1,
                    'start_date': start_date,
                    'end_date': end_date,
                    'is_rented': false,
                }
                session.execute(query, params)
                session.commit()

        else:
            return []


def bookroom():
    return pc.vstack(
        pc.heading("Book a Room:", font_size="2em"),
        pc.text("From Date: "),
        pc.input_group(
            pc.input(type_="date",
                     on_change=SearchState.set_end_date)
        ),
        pc.text("End Date: "),
        pc.input_group(
            pc.input(type_="date",
                     on_change=SearchState.set_start_date)
        ),
        pc.text("Capacity: "),
        pc.number_input(
            on_change=SearchState.set_capacity,
        ),
        amenities_checklist(),
        view_rooms(),
    )


def view_rooms():
    return pc.table_container(
        pc.table(
            pc.table_caption("Rooms"),
            pc.thead(
                pc.tr(*[pc.th(column) for column in room_columns])
            ),
            pc.tbody(
                *[
                    pc.tr(*[pc.td(item) for item in row], on_click=lambda: SearchState.make_booking)
                    for row in get_available_rooms()
                ]
            ),
        )
    )


def get_checkbox(item):
    return pc.checkbox(
        item, color_scheme="green", size="sm"
    )


def amenities_checklist():
    checkboxes = []
    for amenity in get_amenities():
        checkboxes.append(get_checkbox(amenity))

    return pc.vstack(
        *checkboxes
    )
