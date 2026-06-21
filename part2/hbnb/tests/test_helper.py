#!/usr/bin/python3
"""Shared test helpers."""
import uuid


def unique_email(prefix="user"):
    """Generate a unique email so repeated setUp() calls never collide,
    since the facade's in-memory repos persist across test methods."""
    return f"{prefix}.{uuid.uuid4().hex[:8]}@example.com"
