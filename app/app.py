"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from sqlalchemy import text

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

DUMMY_DATA_INSERT = True

if DUMMY_DATA_INSERT:
    # read the SQL queries from the file
    with open('dummy_data.sql', 'r') as f:
        queries = f.read().split(";")

    # execute the SQL queries
    with pc.session() as session:
        for query in queries:
            session.execute(text(query))
        session.commit()
