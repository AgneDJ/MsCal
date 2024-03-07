"""CRUD operations."""

from model import db, User, connect_to_db
from sqlalchemy import insert, or_, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
import os
from datetime import date, datetime


def create_user(name, email):
    """Create and return a new user."""

    user = User(user_name=name, user_email=email,
                user_password="", user_avatar="")

    return user


def get_today():
    """Retrieves today's date"""
    today = date.today()

    return today
