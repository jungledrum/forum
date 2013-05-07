from django.shortcuts import render, redirect
from datetime import date
from bson.objectid import ObjectId
from posts.utils import init_db, is_login
from django.http import HttpResponse

db = init_db()

def create(request, post_id):
    if not is_login(request):
        return redirect('/users/new/')
    content = request.POST['content']
    comment = {'content':content, 'post_id':ObjectId(post_id), 'username':request.session['username']}
    comments = db.comments
    comment_id = comments.insert(comment)
    return HttpResponse(comment_id)

def destroy(request, post_id, comment_id):
    if not is_login(request):
        return redirect('/users/new/')
    comment = db.comments.find_one({'_id':ObjectId(comment_id)})
    if comment.get('username') == request.session['username']:
        db.comments.remove({'_id':ObjectId(comment_id)})
    return redirect('/posts/%s/' % post_id)