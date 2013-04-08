from django.shortcuts import render, get_object_or_404, redirect
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry, CommentEntry, VotingEntry
from django.shortcuts import render_to_response
from django.http import HttpResponse

def voting_load(request):
    votes = VotingEntry.objects.filter(root_id=request.GET['id'])
    value = 0
    for vote in votes:
        value += vote.vote
    return HttpResponse(str(value))

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

