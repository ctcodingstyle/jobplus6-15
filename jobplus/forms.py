# -*- coding: utf-8 -*-
'''form.py
实现表单模型
'''
# TODO 实现 forms.py 文件
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User
from flask import flash

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            flash('登录失败', 'danger')
            raise ValidationError('该邮箱未注册')


class UserProfileForm(FlaskForm):
    name = StringField('姓名')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码（不填写保持不变）', validators=[Required(), Length(6, 24)])
    phone = StringField('手机号')
    work_year = IntegerField('工作年限')
    resume_uri = StringField('简历地址')
    submit = SubmitField('提交')


class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码（不填写保持不变）', validators=[Required(), Length(6, 24)])
    phone = StringField('手机号')
    city = IntegerField('地址')
    website = StringField('公司网站')
    logo_uri = StringField('Logo')
    introduction = StringField('一句话描述')
    description = TextAreaField('公司详情')
    submit = SubmitField('提交')
