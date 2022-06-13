# -*- coding:utf-8 -*-
from flask_login import UserMixin
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(255), nullable=False)
    email = db.Column('email', db.String(255), nullable=False)
    password = db.Column('password', db.String(255))
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=func.now())


class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    datetime = db.Column('datetime', db.DateTime(timezone=True), nullable=False,
                         info={'label': u'วันที่ต้องการนัดหมาย'})
    purpose = db.Column('purpose', db.String(), nullable=False,
                        info={'label': u'จุดประสงค์',
                              'choices': [(c, c) for c in [u'checkup', u'Wellness', u'NNN']]})
    detail = db.Column('detail', db.Text(), nullable=True,
                       info={'label': u'รายละเอียด'})
    user_id = db.Column('user_id', db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=func.now())
    user = db.relation(User, backref=db.backref('appointments', lazy='dynamic'))
    confirmed_at = db.Column('confirmed_at', db.DateTime(timezone=True))

