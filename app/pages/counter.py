"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging

import pynecone as pc

from app.basestate import BaseState


logger = logging.getLogger(__name__)


class CounterBaseState(BaseState):
    count: int = 0

    def increment_by_2(self):
        self.count += 2
        logger.info("INCREMENT BY 2")

    def decrement_by_2(self):
        self.count -= 2
        logger.info("DECREMENT BY 2")


def counter():
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=CounterBaseState.decrement_by_2,
        ),
        pc.heading(CounterBaseState.count, font_size="2em"),
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=CounterBaseState.increment_by_2,
        ),
    )
