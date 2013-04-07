from django.shortcuts import render, get_object_or_404, redirect
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry, CommentEntry
from django.shortcuts import render_to_response


def comments_load(request):
    comments = CommentEntry.objects.filter(root_id=request.GET['id'], parent_id=-1).order_by('-created')
    return render_to_response('comments_load.html', { 'comments': comments })

@csrf_exempt
@login_required
def comments_add(request):
    comment = CommentEntry(root_id=request.POST['id'], body=request.POST['body'], user=request.user, parent_id=-1)
    comment.save();
    return render_to_response('profile_add_skill.html')
