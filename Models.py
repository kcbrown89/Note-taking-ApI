from sqlalchemy import Integer,Column,String,TIMESTAMP
from sqlalchemy.orm import relationship,DeclarativeBase
import datetime

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    title=Column(String, index=True,nullable=False)
    content=Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())
