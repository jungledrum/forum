from django.shortcuts import render, redirect
from datetime import date
from bson.objectid import ObjectId
from posts.utils import init_db, is_login
from django.http import HttpResponse

db = init_db()

def index(request, page=1):
    posts, pages_num = paging(db.posts.find(), page)
    context = {'posts':posts, 'session':request.session, 'pages_num':pages_num, 'page':int(page)}
    return render(request, 'posts/index.html', context)

def show(request, post_id, page=1):
    post = db.posts.find_one({'_id':ObjectId(post_id)})
    comments = db.comments.find({'post_id':ObjectId(post_id)})
    comments, pages_num = paging(comments, page)
    context = {'post':post, 'comments':comments, 'session':request.session, 
                'pages_num':pages_num, 'page':int(page)}
    return render(request, 'posts/show.html', context)

def create(request):
    if not is_login(request):
        return redirect('/users/new/')
    title = request.POST['title']
    content = request.POST['content']
    post = {'title':title, 'content':content, 'username':request.session['username']}
    posts = db.posts
    post_id = posts.insert(post)
    return HttpResponse(post_id)

def destroy(request, post_id):
    if not is_login(request):
        return redirect('/users/new/')
    post = db.posts.find_one({'_id':ObjectId(post_id)})
    if request.session['username'] == post.get('username'):
        db.posts.remove({'_id':ObjectId(post_id)})
    return redirect('/posts/')

def paging(items, page):
    num_per_page = 5
    skip = (int(page) - 1) * num_per_page
    pages_num = items.count() / num_per_page
    if items.count() % num_per_page > 0:
        pages_num = pages_num + 1
    pages_num = range(1, pages_num+1)
    return items.skip(skip).limit(num_per_page), pages_num