from django.shortcuts import render, get_object_or_404
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry
from django.shortcuts import render_to_response

def projects(request):
    return render_to_response('projects.html')