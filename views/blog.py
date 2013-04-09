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
    for post in posts:    
        post.body = render_to_html(post.body)
    return render_to_response('blog.html', { 'posts': posts, 'user': request.user }) #LINK [[<url>|<text>]]
    
import re
def render_to_html(text):
    text = text.replace('\n', '<br />')
    text = re.sub(r"'''(.*?)'''", r"<strong>\1</strong>", text)
    text = re.sub(r"''(.*?)''", r"<em>\1</em>", text)
    text = re.sub(r"\[\[(.*?)\|(.*?)\]\]", r"<a target='_blank' href='\1'>\2</a>", text)
    return text
    
