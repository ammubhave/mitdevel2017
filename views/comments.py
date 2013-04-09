from django.shortcuts import render, get_object_or_404, redirect
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry, CommentEntry
from django.shortcuts import render_to_response
from django.http import HttpResponse

def comments_load(request):
    comments = CommentEntry.objects.filter(root_id=request.GET['id'], parent_id=-1).order_by('-created')
    #for comment in comments:
        
    return render_to_response('comments_load.html', { 'comments': comments, 'user': request.user })

@csrf_exempt
@login_required
def comments_add(request):
    comment = CommentEntry(root_id=request.POST['id'], body=request.POST['body'], user=request.user, parent_id=-1)
    comment.save();
    return HttpResponse('1')

@csrf_exempt
@login_required
def comments_delete(request):
    comment = CommentEntry.objects.get(id=request.GET['id'], user=request.user, parent_id=-1)
    comment.delete();
    return HttpResponse('1')
