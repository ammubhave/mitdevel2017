import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from openshift.models import SkillEntry

def members(request):
    users = User.objects.all().order_by('first_name')
    skills = set(SkillEntry.objects.all().values_list('skill_name', flat=True))
    import random
    skills = random.sample(skills, 10)
    
    if 'filter' in request.GET:
        pfilter = request.GET['filter']
        if pfilter is not None and pfilter != '':
            users = SkillEntry.objects.filter(skill_name=str(pfilter).lower()).values_list('user', flat=True)
            users = User.objects.filter(id__in = users)
    #for user in users:
      #  skills = []
     #   SkillEntry.objects.filter(user=user)
        #skills.append(skill.name)
        #user.skills = skills.join(',')
    return render(request, 'members.html', { 'users': users, 'skills': skills } )
