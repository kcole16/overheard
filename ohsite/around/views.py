from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import Account
from around.models import Post, Comment
from around.forms import PostForm, CommentForm

from datetime import datetime

#def create_user(request):

def comments(request, post_id):
	no_comments = False
	post_id=post_id
	print post_id
	try:
		comments = Comment.objects.filter(post_id=post_id)
	except ObjectDoesNotExist:
		no_comments = True
		return render_to_response('around/comments.html',{'no_comments':no_comments, 'post_id':post_id}, context_instance=RequestContext(request))
	else:
		return render_to_response('around/comments.html',{'no_comments':no_comments, 'comments':comments, 'post_id':post_id}, context_instance=RequestContext(request))


@login_required
def create_post(request):
	created = False
	if request.POST:
		form = PostForm(request.POST)
		user = Account.objects.get(id=request.user.id)
		form.is_valid()
		content_to_use = form.cleaned_data
		content= str(content_to_use['content'])
		date_posted = datetime.now()
		post = Post.create(user, content, date_posted)
		post.save()
		created = True
		return render_to_response('around/create_post.html', {'created':created}, context_instance=RequestContext(request))
	else:
		return render_to_response('around/create_post.html', context_instance=RequestContext(request))

@login_required
def add_comment(request, post_id):
	created = False
	post_id = post_id
	if request.POST:
		form = CommentForm(request.POST)
		user = Account.objects.get(id=request.user.id)
		post = Post.objects.get(id=post_id)
		form.is_valid()
		content_to_use = form.cleaned_data
		content= str(content_to_use['content'])
		date_posted = datetime.now()
		comment = Comment.create(user, post, content, date_posted)
		comment.save()
		created = True
		return render_to_response('around/add_comment.html', {'created':created, 'post_id':post_id}, context_instance=RequestContext(request))
	else:
		return render_to_response('around/add_comment.html', {'created':created, 'post_id':post_id}, context_instance=RequestContext(request))

#@login_required
#def add_comment(request, post_id):




