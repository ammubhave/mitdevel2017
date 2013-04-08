from django.shortcuts import render, get_object_or_404, redirect 
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import CollaboratorsEntry, ProjectEntry
from django.shortcuts import render_to_response
from django.http import HttpResponse

def collaborators(request):
    #collaborators = CollaboratorsEntry.objects.filter(project = request.id)
    collaborators = CollaboratorsEntry.objects.all()
    return render_to_response('projects.html', { 'collaborators': collaborators })

@csrf_exempt
@login_required
def collaborators_add(request):
    if 'project_id' not in request.POST:
        return HttpResponse('0')
    project = ProjectEntry.objects.get(id=request.POST['project_id'])
    collaborators = CollaboratorsEntry.objects.filter(project = project.id, user = request.user)
    if len(collaborators) == 0:
        collaborator = CollaboratorsEntry(project = project,
                        user = request.user)
        collaborator.save()
    
    return HttpResponse('1')

@csrf_exempt
@login_required
def collaborators_delete(request):
    if 'project_id' not in request.POST:
        return HttpResponse('0')
    project = ProjectEntry.objects.get(id=request.POST['project_id'])
    collaborators = CollaboratorsEntry.objects.filter(project_name = project_name)
    if len(collaborators) == 0:
        collaborator = collaborators[0]
        collaborator.delete()
    
    return HttpResponse('1')
