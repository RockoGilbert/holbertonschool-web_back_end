#!/usr/bin/env python3
"""Creates a basic_Auth class that inherits from Auth"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Authorization Class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Authorization"""

        if (
            not authorization_header or type(authorization_header) != str
            or "Basic " not in authorization_header
        ):
            return None
        return authorization_header.split()[1]
