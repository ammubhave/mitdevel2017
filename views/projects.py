from django.shortcuts import render, get_object_or_404, redirect
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry
from django.shortcuts import render_to_response

def projects(request):
    projects = ProjectEntry.objects.all()
    import re
    
    for project in projects:
        project.project_description_safe = project.project_description
        project.project_description = project.project_description.replace('\n', '<br />')
        project.project_description = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', project.project_description)
        project.project_description = re.sub(r'_(.*?)_', r'<em>\1</em>', project.project_description)
        project.project_description = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'<a target="_blank" href="\1">\2</a>', project.project_description)
    
    return render_to_response('projects.html', { 'projects': projects, 'user': request.user })
    
@csrf_exempt
@login_required
def projects_add(request):
    project_name = request.POST['projectName']
    project_description = request.POST['projectDesc']
    projects = ProjectEntry.objects.filter(project_name = project_name)
    if len(projects) == 0:
        project = ProjectEntry(project_name = project_name,
                        project_description = project_description,
                        user = request.user)
        project.save()
    
    return redirect('/projects')

@csrf_exempt
@login_required
def projects_update(request):
    project_id = request.POST['projectId']
    project_name = request.POST['projectName']
    project_description = request.POST['projectDesc']
    project = ProjectEntry.objects.filter(id = project_id, user=request.user)
    if len(project) > 0:
        project = project[0]
        project.project_name = project_name
        project.project_description = project_description
        project.save()
    
    return redirect('/projects')
    
@login_required
def projects_delete(request):
    project_id = request.GET['id']
    project = ProjectEntry.objects.filter(id = project_id, user=request.user.id)
    if len(project) > 0:
        project = project[0]
        project.delete()
    
    return redirect('/projects')
