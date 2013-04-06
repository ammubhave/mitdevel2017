import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from openshift.models import SkillEntry
#from openshift.models import UserProfile, SkillEntry

def members_profile(request, username):
    member = get_object_or_404(User.objects.filter(username=username))
    skills = SkillEntry.objects.filter(user=member.id).order_by('proficiency')
    for skill in skills:
        skill.label_class = 'default'
        if skill.proficiency == SkillEntry.STUDENT:
            skill.proficiency_text = 'Student'
            skill.label_class = 'info'
        elif skill.proficiency == SkillEntry.BEGINNER:
            skill.proficiency_text = 'Beginner'
            skill.label_class = 'success'
        elif skill.proficiency == SkillEntry.INTERMEDIATE:
            skill.proficiency_text = 'Intermediate'
            skill.label_class = 'warning'
        elif skill.proficiency == SkillEntry.ADVANCED:
            skill.proficiency_text = 'Advanced'
            skill.label_class = 'important'
    #for user in users:
      #  skills = []
     #   SkillEntry.objects.filter(user=user)
        #skills.append(skill.name)
        #user.skills = skills.join(',')
    return render(request, 'members_profile.html', { 'member': member, 'skills': skills } )
