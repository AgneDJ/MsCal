"""Models for MsCal app."""

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets


db = SQLAlchemy()


class User(db.Model):
    """A user data."""

    __tablename__ = "user_data"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String)
    user_avatar = db.Column(db.String)

    def __repr__(self):
        return f"{self.user_name}"


def connect_to_db(flask_app, db_uri="postgresql:///calendar_data", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    with app.app_context():
        db.create_all()


# A basic health profile contains

# Age
# Weight
# Height
# Allergies
# Addictions
# Period date
# Period information
# Sexual activity information
# Menstrual cycle:


#         Tracking

# Days to next cycle
# Symptoms log
# Cycle log
# Cycle duration
# Weight changes
# Activity log during cycle
# Mood log


#         Push Notifications for

# Upcoming period
# Daily log entries
# Next phase of the cycle
# Enter mood
# Medication time
# Ovulation
# Fertility


#         Suggestions and Tips

# PMS
# Medical information
# Daily health tips


#         Graphical representations of

# Menstrual cycle
# Fertility
# Ovulation
# Symptoms
# Linking with

# Women fitness trackers
# Social media


# cronofy api calendar

#         https://app.cronofy.com/oauth/applications/65e812845f5ce44a48d306d2/authorizations/65e81319bdd1b746d82f3d11
