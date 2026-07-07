#!/usr/bin/python3
"""Place model."""

from app.models.base_model import BaseModel
from app.models.user import User
from app.extensions import db


class Place(BaseModel):
    """Place class for property listings."""
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        """Add an empty amenity to the place."""
        self.amenities.append(amenity)
        self.save()