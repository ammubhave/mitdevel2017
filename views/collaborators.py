from django.shortcuts import render, get_object_or_404, redirect 
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import CollaboratorsEntry
from django.shortcuts import render_to_response
from django.http import HttpResponse

def collaborators(request):
    collaborators = CollaboratorsEntry.objects.all()
    return render_to_response('projects.html', { 'collaborators': collaborators })

@login_required
def collaborators_add(request):
    if 'projectName' not in request.POST:
        return redirect('/projects')
    project = request.GET['id']
    collaborators = CollaboratorsEntry.objects.filter(project_name = project_name)
    if len(collaborators) == 0:
        collaborator = CollaboratorsEntry(project = project_name,
                        user = request.user)
        collaborator.save()
    
    return redirect('/projects')

@login_required
def collaborators_delete(request):
    if 'projectName' not in request.POST:
        return redirect('/projects')
    project = request.GET['id']
    collaborators = CollaboratorsEntry.objects.filter(project_name = project_name)
    if len(collaborators) == 0:
        collaborator = collaborator[0]
        collaborator.delete()
    
    return redirect('/projects')
