from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from bson.objectid import ObjectId

from posts.utils import init_db, login_required


db = init_db()


@require_POST
@login_required
def create(request, post_id):
    content = request.POST['content']
    comment = {'content': content, 'post_id': ObjectId(post_id),
               'username': request.session['username']}
    comments = db.comments
    comment_id = comments.insert(comment)
    context = {"comment_id": comment_id, "post_id": post_id,
               "comment": comment}
    return render(request, 'comments/show.html', context)


@require_GET
@login_required
def destroy(request, post_id, comment_id):
    comment = db.comments.find_one({'_id': ObjectId(comment_id)})
    if comment.get('username') == request.session['username']:
        db.comments.remove({'_id': ObjectId(comment_id)})
    return redirect(reverse('posts.views.posts_view.show', args=(post_id,)))
