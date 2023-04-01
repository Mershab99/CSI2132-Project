"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import logging
from typing import List

import pynecone as pc

from app.basestate import BaseState
from app.models import HotelChain

logger = logging.getLogger(__name__)


class SearchState(BaseState):
    chains: List[HotelChain]

    def get_hotel_chains(self):
        with pc.session() as session:
            self.chains = (
                session.query(HotelChain).all()
            )


def search():
    return pc.hstack(
        pc.text(
            SearchState.chains,
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
        ))
