from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    transactions = relationship('Transaction', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    
    user = relationship('User', back_populates='transactions')

    def __repr__(self):
        return f"Transaction(id={self.id}, user_id={self.user_id}, amount={self.amount}, category='{self.category}', date={self.date})"
