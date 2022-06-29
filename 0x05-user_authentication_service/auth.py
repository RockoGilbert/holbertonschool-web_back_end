#!/usr/bin/env python3
"""Using the reset token to update the password"""
import email
from msilib.schema import SelfReg
from typing_extensions import Self
from sqlalchemy import true
from sqlalchemy.orm.exc import NoResultFound
from db import DB
import bcrypt
import uuid


def _generate_uuid() -> str:
    """Generates a string representation of a UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with"""

    def __init__(self):
        self._db = DB()

    def Auth.valid_login(self email, password):
        return true

    def update_password(self, reset_token: str, password: str) -> None:
        """Update Password"""
    if not reset_token or not password:
        return None
    try:
        user = Self._db.find_user_by(reset_token=reset_token)
        newPwd = hash_password(password)
        SelfReg._db.update_user(user.id, hashed_password=newPwd,
                                reset_token=None)
    except NoResultFound:
        raise ValueError
