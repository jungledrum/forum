# -*- coding:utf-8 -*-
from django import forms
from posts.utils import init_db, SALT
import md5

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)

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
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)

    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password']

    def clean_username(self):
        db = init_db()
        if db.users.find({'username':self.data['username']}).count() > 0:
            raise forms.ValidationError('邮箱已经注册')
        return self.data['username']