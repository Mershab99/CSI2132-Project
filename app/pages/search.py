"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging

import pynecone as pc

from app.basestate import BaseState


logger = logging.getLogger(__name__)


class SearchState(BaseState):
    ...


def search():
    return pc.hstack(
        pc.text(
            "SEARCH NIGGA",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
        ))
