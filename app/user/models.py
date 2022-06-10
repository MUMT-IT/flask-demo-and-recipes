from sqlalchemy import func

from app.main import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    email = db.Column('email', db.String(255), nullable=False)
    password = db.Column('password', db.String(255))
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=func.now())


class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    datetime = db.Column('datetime', db.DateTime(timezone=True), nullable=False)
    user_id = db.Column('user_id', db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=func.now())

