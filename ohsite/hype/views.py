from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from hype.models import Topic, Location, HypeComment
from hype.forms import CommentForm
from core.models import Account
from core.keys import *

import twitter

def get_topics(request):
	api = twitter.Api(consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

	statuses = api.GetTrendsWoeid(id = 2514815, exclude='hashtags')
	for status in statuses:
		try:
			topic = Topic.create(status.name)
			topic.save()
		except IntegrityError:
			pass

	return HttpResponseRedirect('/hype/home')


def home(request):
	topics = Topic.objects.order_by('-id')[:10]
	counts = HypeComment.objects.raw('select t.id, count(*) from hype_topic t inner join hype_hypecomment c on c.topic_id = t.id group by t.id;  ')
	return render_to_response('hype/home.html', {'topics':topics, 'counts':counts}, context_instance=RequestContext(request))


def comments(request, topic_id):
	no_comments = False
	topic_id=topic_id

	try:
		comments = HypeComment.objects.filter(topic_id=topic_id)
	except ObjectDoesNotExist:
		no_comments = True
		return render_to_response('hype/comments.html',{'no_comments':no_comments, 'topic_id':topic_id}, context_instance=RequestContext(request))
	else:
		return render_to_response('hype/comments.html',{'no_comments':no_comments, 'comments':comments, 'topic_id':topic_id}, context_instance=RequestContext(request))


def add_comment(request, topic_id):
	created = False
	topic_id = topic_id
	if request.POST:
		form = CommentForm(request.POST)
		user = Account.objects.get(id=request.user.id)
		topic = Topic.objects.get(id=topic_id)
		form.is_valid()
		content_to_use = form.cleaned_data
		content= str(content_to_use['content'])
		comment = HypeComment.create(user, topic, content)
		comment.save()
		created = True
		return render_to_response('hype/add_comment.html', {'created':created, 'topic_id':topic_id}, context_instance=RequestContext(request))
	else:
		return render_to_response('hype/add_comment.html', {'created':created, 'topic_id':topic_id}, context_instance=RequestContext(request))




