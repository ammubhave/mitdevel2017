import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry
#from openshift.models import UserProfile, SkillEntry

'''Display a member's profile: his skills, interests, website, etc.
'''
def members_profile(request, username):
    member = get_object_or_404(User.objects.filter(username=username))
    skills = SkillEntry.objects.filter(user=member.id).order_by('proficiency')
    interests = InterestEntry.objects.filter(user=member.id).order_by('level')
    websites = WebsiteEntry.objects.filter(user=member.id)

    # TODO: The code is redundant, too many places same code is written. Use a better method to lookup.
    for interest in interests:
        interest.label_class = 'default'
        if interest.level == InterestEntry.NOT_MUCH_INTERESTED:
            interest.level_text = 'Not much Interested'
            interest.label_class = 'info'
        elif interest.level == InterestEntry.INTERESTED:
            interest.level_text = 'Interested'
            interest.label_class = 'success'
        elif interest.level == InterestEntry.VERY_INTERESTED:
            interest.level_text = 'Very Interested'
            interest.label_class = 'important'
        
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

    for website in websites:
        website.label_class = 'default'
        if website.classification == WebsiteEntry.PERSONAL:
            website.classification_text = 'Personal'
            website.label_class = 'info'
        elif website.classification == WebsiteEntry.WORK:
            website.classification_text = 'Work'
            website.label_class = 'success'
        
    return render(request, 'members_profile.html', { 'member': member, 'skills': skills, 'interests': interests, 'websites': websites } )
