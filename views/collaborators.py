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
    collaborators = CollaboratorstEntry.objects.filter(project_name = project_name)
    if len(collaborators) == 0:
        collaborator = ProjectEntry(project = project_name,
                        user = request.user)
        collaborator.save()
    
    return redirect('/projects')

@login_required
def collaborators_delete(request):
    if 'projectName' not in request.POST:
        return redirect('/projects')
    project = request.GET['id']
    collaborators = CollaboratorstEntry.objects.filter(project_name = project_name)
    if len(collaborators) == 0:
        collaborator = ProjectEntry(project = request.project.id,
                        user = request.user)
        collaborator.save()
    
    return redirect('/projects')

@csrf_exempt
@login_required
def voting_vote(request):
    votes = VotingEntry.objects.filter(root_id=request.POST['id'], user=request.user.id)
    vote_data = int(request.POST['vote'])
    if vote_data not in (1, -1):
        return HttpResponse('0')
    if len(votes) == 0: # check if user has already voted        
        vote = VotingEntry(root_id=request.POST['id'], user=request.user, vote=int(request.POST['vote']))
        vote.save()
    else:
        vote = votes[0]
        if vote.vote != int(request.POST['vote']):
            vote.vote = int(request.POST['vote'])
            vote.save()
    return HttpResponse('1')
