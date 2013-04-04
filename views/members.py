import os
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User

def members(request):
    users = User.objects.all()
    return render(request, 'members.html', { 'users': users } )
