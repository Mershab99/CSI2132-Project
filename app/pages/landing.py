"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging

import pynecone as pc

from app.basestate import DUMMY_DATA, BaseState

logger = logging.getLogger(__name__)

columns = ["start_date", "end_date", "is_rented"]


def get_booking_list():
    if not DUMMY_DATA:
        with pc.session() as session:
            result = session.execute("SELECT * FROM booking")
            return [row for row in result]

    else:
        return []
def landing():
    print("Auth state: admin {}", BaseState.admin)
    return pc.cond(BaseState.admin,
                   view_booking(),
                   pc.link(
                       pc.button(
                           "Book a Room",
                           border_radius="1em",
                           box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                           background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                           box_sizing="border-box",
                           color="white",
                           _hover={
                               "opacity": 0.85,
                           },
                       ),
                       href="/bookroom",
                       color="rgb(107,99,246)",
                       button=True,
                   ), )


def view_booking():
    return pc.table_container(
        pc.table(
            pc.table_caption("Booking Table"),
            pc.thead(
                pc.tr(*[pc.th(column) for column in columns])
            ),
            pc.tbody(
                *[
                    pc.tr(*[pc.td(item) for item in row])
                    for row in get_booking_list()
                ]
            ),
        )
    )
