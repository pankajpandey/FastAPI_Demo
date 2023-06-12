from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    address = Column(Text())
    type = Column(String(20))
    rent = Column(Integer)