#!/usr/bin/python3
"""Base model for all HBnB entities."""

from app import db
import uuid
from datetime import datetime


class BaseModel(db.Model):
    """Base class containing common attributes/methods for models."""

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Update the updated at timestamp."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update object attributes using a dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.save()
