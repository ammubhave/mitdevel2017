from django.shortcuts import render, get_object_or_404
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import BlogEntry
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

''' Display the profile of logged in user. Allow changes
'''

def blog(request): 
    #posts = CommentEntry.objects.filter(root_id=request.GET['id'], parent_id=-1).order_by('-created')
    posts = BlogEntry.objects.all().order_by('-created')
    
    import re
    for post in posts:
        post.body = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', post.body)
        post.body = re.sub(r'_(.*?)_', r'<em>\1</em>', post.body)
        post.body = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'<a target="_blank" href="\1">\2</a>', post.body)
    return render_to_response('blog.html', { 'posts': posts, 'user': request.user })
