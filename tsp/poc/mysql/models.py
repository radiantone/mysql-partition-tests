import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime, Date
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base(name="Base")


class Data(Base):
    __tablename__ = "tsp_tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(30))
    value = Column(Text)
    date = Column(Date, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"Data(id={self.id!r}, key={self.key!r}, value={self.value!r})"
