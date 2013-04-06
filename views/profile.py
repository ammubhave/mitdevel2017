from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry

@login_required
def profile(request): 
    skills = SkillEntry.objects.filter(user = request.user.id).order_by('proficiency')
    for skill in skills:
        skill.label_class = 'default'
        if skill.proficiency == SkillEntry.STUDENT:
            skill.label_class = 'info'
        elif skill.proficiency == SkillEntry.BEGINNER:
            skill.label_class = 'success'
        elif skill.proficiency == SkillEntry.INTERMEDIATE:
            skill.label_class = 'warning'
        elif skill.proficiency == SkillEntry.ADVANCED:
            skill.label_class = 'important'
    return render(request, 'profile.html', { 'user': request.user, 'skills': skills } )
    
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
    
@csrf_exempt
@login_required
def remove_skill(request):
    skill_name = str(request.POST['skill_name']).lower()
    
    skill = get_object_or_404(SkillEntry.objects.filter(skill_name = skill_name, user = request.user))
    skill.delete()
    
    return render(request, 'profile_add_skill.html', { 'success': True } )
