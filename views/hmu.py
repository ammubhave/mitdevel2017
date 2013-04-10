import os
from django.shortcuts import render_to_response

def hmu(request):
    return render_to_response('hmu.html', { 'user': request.user })
