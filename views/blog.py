from django.shortcuts import render, get_object_or_404
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import BlogEntry
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

import openshift.lib.formatting_engine as formatting_engine

''' Display the profile of logged in user. Allow changes
'''

def blog(request): 
    #posts = CommentEntry.objects.filter(root_id=request.GET['id'], parent_id=-1).order_by('-created')
    posts = BlogEntry.objects.all().order_by('-created')
    
    import re
    for post in posts:
        post.body = formatting_engine.render_to_html(post.body)
    return render_to_response('blog.html', { 'posts': posts, 'user': request.user })
