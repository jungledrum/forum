from django.shortcuts import render, redirect
from datetime import date
from bson.objectid import ObjectId
from posts.utils import init_db, SALT
from posts.form import LoginForm, RegisterForm
import md5

db = init_db()

def new(request):
    loginform = LoginForm()
    registerform = RegisterForm()
    return render(request, 'users/new.html', {'loginform':loginform, 'registerform':registerform})

def login(request):
    username = request.POST['username']
    loginform = LoginForm(request.POST)
    registerform = RegisterForm()
    if not loginform.is_valid():
        return render(request, 'users/new.html', {'loginform':loginform, 'registerform':registerform})
    user = db.users.find_one({'username':username})
    request.session['username'] = username
    request.session['uid'] = user['_id']
    return redirect('/posts/')

def logout(request):
    del request.session['username']
    del request.session['uid']
    return redirect('/users/new/')

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    loginform = LoginForm()
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        return render(request, 'users/new.html', {'loginform':loginform, 'registerform':registerform})
    m = md5.new()
    m.update(SALT)
    m.update(password)
    user = {'username':username, 'password':m.hexdigest()}
    user_id = db.users.insert(user)
    request.session['username'] = username
    request.session['uid'] = user_id
    return redirect('/posts/')

def change_password(request):
    pass

def reset_password(request):
    pass