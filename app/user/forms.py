# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from wtforms_alchemy import model_form_factory, QuerySelectField

from app.main import db
from app.models import Appointment, User

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[Length(min=10, message=u'สั้นเกินไป'),
                                             Email(message=u'อีเมลไม่ถูกต้อง'), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6),
                                                     DataRequired()])
    confirmed_password = PasswordField('Confirm Password', validators=[EqualTo('password')])


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        only = ['datetime', 'detail', 'purpose']

    user = QuerySelectField('User', query_factory=lambda: User.query.all(),
                            get_label='name', blank_text='Select user..', allow_blank=False)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Length(min=10, message=u'สั้นเกินไป'),
                                             Email(message=u'อีเมลไม่ถูกต้อง'), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6),
                                                     DataRequired()])
