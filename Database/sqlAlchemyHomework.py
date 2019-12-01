from sqlalchemy.orm import create_engine, Session
from sqlalchemy.orm import sessionmaker
engine = create_engine("/web/Sqlite-Data/example.db")
session = Session(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()