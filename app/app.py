"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from app.pages.counter import counter
from app.pages.index import index
from app.pages.test import test

from .state import BaseState

app = pc.App(state=BaseState)
app.add_page(counter, route='/counter')
app.add_page(index, route='/')
app.add_page(test)
app.compile()
