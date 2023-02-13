from __future__ import annotations

import pynecone as pc
import sqlmodel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


class HotelChain(pc.Model, table=True):
    chain_name: str




