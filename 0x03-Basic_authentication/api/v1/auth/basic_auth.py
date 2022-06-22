#!/usr/bin/env python3
"""Creates a basic_Auth class that inherits from Auth"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Authorization Class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the Authorization"""

        if (
            not authorization_header or type(authorization_header) != str
            or "Basic " not in authorization_header
        ):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decode base64 authorization header"""

        if not base64_authorization_header or type(base64_authorization_header
                                                   ) != str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except Exception:
            return None

        return decoded

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> str(str, str):
        """ Extract User Credentials """
        if (
            not decoded_base64_authorization_header
            or type(decoded_base64_authorization_header) != str
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))
