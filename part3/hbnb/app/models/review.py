#!/usr/bin/python3
"""Review model."""

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place
from app.extensions import db


class Review(BaseModel):
    """Review class for place reviews."""
    __tablename__ = 'reviews'

    text = db.Column(db.String(256), nullable=False)
    rating = db.Column(db.Integer, nullable=False)