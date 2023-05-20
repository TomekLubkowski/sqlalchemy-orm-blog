from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "mysql+pymysql://root:L3naLe0n@localhost:3306/Blog"
)

Session = sessionmaker(bind=engine)
session = Session()

