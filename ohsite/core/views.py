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

from around.models import Post, Comment

@login_required
def home(request):
	posts = []
	no_posts = False
	try:
		posts=Post.objects.all()
	except ObjectDoesNotExist:
		no_posts=True
		return render_to_response('core/home.html',{'posts':posts, 'no_posts':no_posts}, context_instance=RequestContext(request))
	else:
		return render_to_response('core/home.html',{'posts':posts}, context_instance=RequestContext(request))

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
