#!/usr/bin/env python3
"""Authenticates the user"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password:str) -> User:
        """Registers a new user"""
        user = self._db.find_user_by(email=email)
        hashed_password = _hash_password(password)
        if user:
            raise ValueError(f'User {email} already exists')
        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Credentials validation """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user_pw = user.hashed_password
                input_password = password.encode("utf-8")
                return bcrypt.checkpw(input_password, user_pw)
        except (NoResultFound, InvalidRequestError):
            return False
        return False
