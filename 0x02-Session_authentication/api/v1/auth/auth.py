#!/usr/bin/env python3
""" Module of Auth views"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """ Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """ current_user"""
        return None
    
    def session_cookie(self, request=None):
    """session_cookie impl
    """
    if request is None:
        return None
    
    cookie_name = getenv('SESSION_NAME')

    if not cookie_name:
        return None
    
    return request.cookies.get(cookie_name)
