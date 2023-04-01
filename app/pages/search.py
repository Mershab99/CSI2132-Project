"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging
from typing import List

import pynecone as pc

from app.basestate import BaseState
from app.models import HotelChain

logger = logging.getLogger(__name__)


class SearchState(BaseState):

    @pc.var
    def get_hotel_chains(self) -> List[str]:
        with pc.session() as session:
            result = session.execute("SELECT name from hotelchain")
            return [row[0] for row in result]


def search():
    return pc.hstack(
        pc.list(
            items=SearchState.get_hotel_chains,
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
        ))
