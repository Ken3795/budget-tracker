from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///budget_tracker.db"

def get_db():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return engine, Session()

def create_db():
    engine, _ = get_db()
    Base.metadata.create_all(engine)
    print("✅ Database and tables created successfully!")

if __name__ == "__main__":
    create_db()
