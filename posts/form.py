# -*- coding:utf-8 -*-
from django import forms
from posts.utils import init_db, SALT
import md5

class LoginForm(forms.Form):
    username = forms.EmailField(error_messages={'required': '请输入你的邮箱',
                                                'invalid': '邮箱格式不对'})
    password = forms.CharField(widget=forms.PasswordInput(),
                               min_length=8, max_length=20,
                               error_messages={'required': '请输入你的密码',
                                               'max_length': '最长20个字符',
                                               'min_length': '最少8个字符'})

    def clean_password(self):
        db = init_db()
        user = db.users.find_one({'username':self.data['username']})
        if user == None:
            raise forms.ValidationError('用户不存在')
        m = md5.new()
        m.update(SALT)
        m.update(self.data['password'])
        if m.hexdigest() != user['password']:
            raise forms.ValidationError('密码错误')
        return self.data['password']

class RegisterForm(forms.Form):
    username = forms.EmailField(error_messages={'required': '请输入你的邮箱',
                                                'invalid': '邮箱格式不对'})
    password = forms.CharField(widget=forms.PasswordInput(),
                               min_length=8, max_length=20,
                               error_messages={'required': '请输入你的密码',
                                               'max_length': '最长20个字符',
                                               'min_length': '最少8个字符'})
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                min_length=8, max_length=20,
                                error_messages={'required': '请再次输入你的密码',
                                                'max_length': '最长20个字符',
                                                'min_length': '最少8个字符'})

    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('两次输入的密码不一致')
        return self.data['password']

    def clean_username(self):
        db = init_db()
        if db.users.find({'username':self.data['username']}).count() > 0:
            raise forms.ValidationError('邮箱已经注册')
        return self.data['username']