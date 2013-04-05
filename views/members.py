import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
#from openshift.models import UserProfile, SkillEntry

def members(request):
    users = User.objects.all().order_by('first_name')
    #for user in users:
      #  skills = []
     #   SkillEntry.objects.filter(user=user)
        #skills.append(skill.name)
        #user.skills = skills.join(',')
    return render(request, 'members.html', { 'users': users } )
