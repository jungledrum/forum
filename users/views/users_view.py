import md5
from datetime import date

from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from bson.objectid import ObjectId

from posts.utils import init_db, SALT
from posts.form import LoginForm, RegisterForm


db = init_db()


@require_GET
def new(request):
    loginform = LoginForm()
    registerform = RegisterForm()
    context = {'loginform': loginform, 'registerform': registerform}
    return render(request, 'users/new.html', context)


@require_POST
def login(request):
    username = request.POST['username']
    loginform = LoginForm(request.POST)
    registerform = RegisterForm()
    if not loginform.is_valid():
        context = {'loginform': loginform, 'registerform': registerform}
        return render(request, 'users/new.html', context)
    user = db.users.find_one({'username': username})
    request.session['username'] = username
    request.session['uid'] = user['_id']
    return redirect(reverse('posts.views.posts_view.index'))


@require_GET
def logout(request):
    del request.session['username']
    del request.session['uid']
    return redirect(reverse('users.views.users_view.new'))


@require_POST
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    loginform = LoginForm()
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        context = {'loginform': loginform, 'registerform': registerform}
        return render(request, 'users/new.html', context)
    m = md5.new()
    m.update(SALT)
    m.update(password)
    user = {'username': username, 'password': m.hexdigest()}
    user_id = db.users.insert(user)
    request.session['username'] = username
    request.session['uid'] = user_id
    return redirect(reverse('posts.views.posts_view.index'))
