from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Database_url="postgresql://postgres:faith123@localhost:5432/postgres"
engine=create_engine(Database_url)
SessionLocal=sessionmaker(bind=engine)