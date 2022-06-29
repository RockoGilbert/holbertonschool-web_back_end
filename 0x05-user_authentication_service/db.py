#!/usr/bin/env/ python3
"""Complete DB class provided below to implement the add_user method."""
"""DB module"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memorized session object"""
        
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database return the user object
        Args:
            email: email address of the user
            hashed_password: hashed password of the user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by a given key-value pair"""
        
        if not kwargs:
            raise InvalidRequestError
        if not all(key in User.__table__.columns for key in kwargs):
            raise InvalidRequestError
        row = self._session.query(User).filter_by(**kwargs).first()
        if not row:
            raise NoResultFound
        return row

    def update_user(self, user_id: int, **kwargs) -> None:
        """Locates the user to update, then updates user’s
        attributes    
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
        