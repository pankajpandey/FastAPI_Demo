from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote  

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="PanSum3#4$", db="audit_db"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()