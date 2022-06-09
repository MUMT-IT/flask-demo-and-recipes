# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[Length(min=10, message=u'สั้นเกินไป'),
                                             Email(message=u'อีเมลไม่ถูกต้อง'), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6),
                                                     DataRequired()])
    confirmed_password = PasswordField('Confirm Password', validators=[EqualTo('password')])