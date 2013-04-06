import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from openshift.models import SkillEntry, InterestEntry

def members(request):
    users = User.objects.all().order_by('first_name')
    skills = set(SkillEntry.objects.all().values_list('skill_name', flat=True))
    interests = set(InterestEntry.objects.all().values_list('interest_name', flat=True))
    import random
    if len(skills) > 10:
        skills = random.sample(skills, 10)
    if len(interests) > 10:
        interests = random.sample(interests, 10)
    
    pfilter = None
    pfilter_interest = None
    if 'filter' in request.GET:
        pfilter = request.GET['filter']
        if pfilter is not None and pfilter != '':
            users = SkillEntry.objects.filter(skill_name=str(pfilter).lower()).values_list('user', flat=True)
            users = User.objects.filter(id__in = users)
        pfilter = SkillEntry.objects.filter(skill_name=str(pfilter).lower())[0]
    if 'filter_interest' in request.GET:
        pfilter_interest = request.GET['filter_interest']
        if pfilter_interest is not None and pfilter_interest != '':
            users = InterestEntry.objects.filter(interest_name=str(pfilter_interest).lower()).values_list('user', flat=True)
            users = User.objects.filter(id__in = users)
        pfilter_interest = InterestEntry.objects.filter(interest_name=str(pfilter_interest).lower())[0]
    #for user in users:
      #  skills = []
     #   SkillEntry.objects.filter(user=user)
        #skills.append(skill.name)
        #user.skills = skills.join(',')
    return render(request, 'members.html', { 'users': users, 'skills': skills, 'interests': interests, 'pfilter': pfilter, 'pfilter_interest': pfilter_interest } )
