from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry

''' Display the profile of logged in user. Allow changes
'''
@login_required
def profile(request): 
    skills = SkillEntry.objects.filter(user = request.user.id).order_by('proficiency')
    interests = InterestEntry.objects.filter(user = request.user.id).order_by('level')
    websites = WebsiteEntry.objects.filter(user = request.user.id)
    
    # TODO: Redundant. Find better way.
    for interest in interests:
        interest.label_class = 'default'
        if interest.level == InterestEntry.NOT_VERY_INTERESTED:
            interest.level_text = 'Not very Interested'
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
            website.label_class = 'success'
        elif website.classification == WebsiteEntry.WORK:
            website.classification_text = 'Work'
            website.label_class = 'info'

    return render(request, 'profile.html', { 'skills': skills, 'interests': interests, 'websites': websites, 'user': request.user } )
    
    
#TODO: Too many methods below and quite redundant. Use only two methods, add, remove common to all
    
''' Add new skill '''
@csrf_exempt
@login_required
def add_skill(request):
    skill_name =  str(request.POST['skill_name']).lower()
    proficiency = int(request.POST['proficiency'])
    
    success = False
    if len(SkillEntry.objects.filter(skill_name = skill_name, user = request.user)) == 0:
        se = SkillEntry(skill_name = skill_name, proficiency = proficiency, user = request.user)
        se.save()
        success = True
    return render(request, 'profile_add_skill.html', { 'success': success } )
    
''' Remove skill '''
@csrf_exempt
@login_required
def remove_skill(request):
    skill_name = str(request.POST['skill_name']).lower()
    
    skill = get_object_or_404(SkillEntry.objects.filter(skill_name = skill_name, user = request.user))
    skill.delete()
    
    return render(request, 'profile_add_skill.html', { 'success': True } )
    
''' Add interest '''
@csrf_exempt
@login_required
def add_interest(request):
    interest_name =  str(request.POST['interest_name']).lower()
    level = int(request.POST['level'])
    
    success = False
    if len(InterestEntry.objects.filter(interest_name = interest_name, user = request.user)) == 0:
        se = InterestEntry(interest_name = interest_name, level = level, user = request.user)
        se.save()
        success = True
    return render(request, 'profile_add_skill.html', { 'success': success } )
    
''' Remove interest '''
@csrf_exempt
@login_required
def remove_interest(request):
    interest_name = str(request.POST['interest_name']).lower()
    
    interest = get_object_or_404(InterestEntry.objects.filter(interest_name = interest_name, user = request.user))
    interest.delete()
    
    return render(request, 'profile_add_skill.html', { 'success': True } )

''' Add website '''
@csrf_exempt
@login_required
def add_website(request):
    website_url =  str(request.POST['website_url']).lower()
    classification = int(request.POST['classification'])
    
    success = False
    if len(WebsiteEntry.objects.filter(website_url = website_url, user = request.user)) == 0:
        se = WebsiteEntry(website_url = website_url, classification = classification, user = request.user)
        se.save()
        success = True
    return render(request, 'profile_add_skill.html', { 'success': success } )
    
''' Remove website '''
@csrf_exempt
@login_required
def remove_website(request):
    website_url = str(request.POST['website_url']).lower()
    
    website = get_object_or_404(WebsiteEntry.objects.filter(website_url = website_url, user = request.user))
    website.delete()
    
    return render(request, 'profile_add_skill.html', { 'success': True } )
