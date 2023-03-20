"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging

import pynecone as pc

from app.state import State


logger = logging.getLogger(__name__)


class CounterState(State):
    count: int = 0

    def increment_by_2(self):
        self.count += 2

    def decrement_by_2(self):
        self.count -= 2


def counter():
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=CounterState.decrement_by_2,
        ),
        pc.heading(CounterState.count, font_size="2em"),
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=CounterState.increment_by_2,
        ),
    )
