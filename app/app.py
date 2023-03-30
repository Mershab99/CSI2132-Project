"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from sqlalchemy import create_engine, text

import pcconfig
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

DUMMY_DATA_INSERT = False

if DUMMY_DATA_INSERT:
    # create a database engine
    engine = create_engine(pcconfig.config.db_url)

    # read the SQL queries from the file
    with open('dummy_data.sql', 'r') as f:
        queries = f.read().split(";")
        pc.console_log('Well hello there nigga')

    # execute the SQL queries
    with engine.connect() as conn:
        for query in queries:
            if query.strip():
                conn.execute(text(query))

