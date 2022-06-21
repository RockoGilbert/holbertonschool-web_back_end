#!/usr/bin/env python3
"""Creates a basic_Auth class that inherits from Auth"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Authorization Class"""
    pass
