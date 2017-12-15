from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.messages import error
from models import *

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'capp/cappIndex.html', context)

def new(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')

    Course.objects.create(name = request.POST["name"], description = request.POST["description"])

    return redirect('/')

def confdestroy(request, id):
    course_id = id
    return render(request, 'capp/cappDestroy.html', id = course_id)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('capp_index')
