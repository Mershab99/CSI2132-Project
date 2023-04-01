import pynecone as pc

from app.basestate import BaseState

from app.models import HotelChain


#class State(BaseState):

def test():
    return pc.hstack(
        pc.text(
            "Hello World",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
        ))
