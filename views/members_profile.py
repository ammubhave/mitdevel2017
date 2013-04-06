import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
#from openshift.models import UserProfile, SkillEntry

def members_profile(request, username):
    user = get_object_or_404(User.objects.filter(username=username))
    #for user in users:
      #  skills = []
     #   SkillEntry.objects.filter(user=user)
        #skills.append(skill.name)
        #user.skills = skills.join(',')
    return render(request, 'members_profile.html', { 'user': user } )
