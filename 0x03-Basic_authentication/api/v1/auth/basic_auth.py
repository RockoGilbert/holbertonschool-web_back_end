#!/usr/bin/env python3
"""Creates a basic_Auth class that inherits from Auth"""

from base64 import b64decode
from api.v1.auth.auth import Auth
from models.user import User
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """Basic authorization Class"""

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
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except Exception:
            return None

        return decoded

    def extract_user_credentials(
                                self,
                                decoded_base64_authorization_header: str
                                ) -> Tuple[str, str]:
        '''Extract the user credentials'''
        if decoded_base64_authorization_header:
            if type(decoded_base64_authorization_header) is str:
                if decoded_base64_authorization_header.find(":") > 0:
                    return decoded_base64_authorization_header.split(":")
        return None, None

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ User Object From Credentials """
        if (
            not user_email or type(user_email) != str
            or not user_pwd or type(user_pwd) != str
        ):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None

        if user and user[0].is_valid_password(user_pwd):
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
