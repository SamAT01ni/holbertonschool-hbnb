#!/usr/bin/python3
"""Application extensions to stop circular import during test."""

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()
