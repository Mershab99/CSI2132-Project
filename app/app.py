"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from app.pages.counter import counter
from app.pages.index import index
from app.pages.test import test

from app.state import State

app = pc.App(state=State)
app.add_page(counter)
app.add_page(index)
app.add_page(test)
app.compile()
