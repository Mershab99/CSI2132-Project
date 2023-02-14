import pynecone as pc

from app.state import BaseState

from app.models import HotelChain

HotelChain(chain_name='mychain')


class State(BaseState):
    count: int = 0

    def increment_by_2(self):
        self.count += 2

    def decrement_by_2(self):
        self.count -= 2


def test():
    return pc.hstack(
        pc.text(
            "Hello World",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
        ))
