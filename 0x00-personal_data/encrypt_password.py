#!/usr/bin/env python3
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    b = password.encode()
    hashed = hashpw(b, bcrypt.general())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check whether password is valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
