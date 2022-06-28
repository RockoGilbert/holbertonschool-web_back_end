#!/usr/bin/env python3
"""SQLAlchemy model for a database table"""

from db import DB
from user import User

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, NoResultFound

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
