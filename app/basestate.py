import pynecone as pc

DUMMY_DATA: bool = False


class BaseState(pc.State):
    admin: bool = False
