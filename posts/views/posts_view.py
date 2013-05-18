from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from bson.objectid import ObjectId

from posts.utils import init_db, login_required


db = init_db()


@require_GET
@login_required
def index(request, page=1):
    posts, pages_num = paging(db.posts.find(), page)
    context = {'posts': posts, 'session': request.session,
               'pages_num': pages_num, 'page': int(page)}
    return render(request, 'posts/index.html', context)


@require_GET
@login_required
def show(request, post_id, page=1):
    post = db.posts.find_one({'_id': ObjectId(post_id)})
    comments = db.comments.find({'post_id': ObjectId(post_id)})
    comments, pages_num = paging(comments, page)
    context = {'post': post, 'comments': comments, 'session': request.session,
               'pages_num': pages_num, 'page': int(page)}
    return render(request, 'posts/show.html', context)


@require_POST
@login_required
def create(request):
    title = request.POST['title']
    content = request.POST['content']
    post = {'title': title, 'content': content,
            'username': request.session['username']}
    posts = db.posts
    post_id = posts.insert(post)
    return HttpResponse(post_id)


@require_GET
@login_required
def destroy(request, post_id):
    post = db.posts.find_one({'_id': ObjectId(post_id)})
    if request.session['username'] == post.get('username'):
        db.posts.remove({'_id': ObjectId(post_id)})
    return redirect(reverse('posts.views.posts_view.index'))


def paging(items, page):
    num_per_page = 15
    skip = (int(page) - 1) * num_per_page
    pages_num = items.count() / num_per_page
    if items.count() % num_per_page > 0:
        pages_num = pages_num + 1
    pages_num = range(1, pages_num+1)
    return items.skip(skip).limit(num_per_page), pages_num
