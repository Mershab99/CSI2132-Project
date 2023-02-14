from __future__ import annotations

import pynecone as pc
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

import pcconfig


class HotelChain(pc.Model, table=True):
    chain_name: str


graph = create_schema_graph(metadata=MetaData(pcconfig.config.db_url),
                            show_datatypes=False, show_indexes=False)
graph.write_png('er_diagram.png')