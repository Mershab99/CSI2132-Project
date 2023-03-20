"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from app.pages.counter import counter
from app.pages.index import index
from app.pages.test import test
from app.pages.search import search

from app.basestate import BaseState

app = pc.App(state=BaseState)
app.add_page(counter)
app.add_page(index)
app.add_page(test)
app.add_page(search)
app.compile()
