#!/usr/bin/env python3
"""Creating a new class from Auth"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Creates new sesh"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a new session"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str((uuid.uuid4()))
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Create an instance method"""
        if session_id is None and type(session_id) != str:
            return
        return SessionAuth.user_id_by_session_id.get(session_id, None)
