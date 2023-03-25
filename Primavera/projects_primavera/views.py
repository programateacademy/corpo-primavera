from django.shortcuts import render, get_object_or_404,redirect
from .models import Project, Activities
from .forms import ActivitiesForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime


def render_projects(request):
    projects = Project.objects.filter(date__lte=datetime.now()).order_by('-date')
    return render(request, 'projects.html', {'projects':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk= project_id)
    return render (request, 'project_detail.html', {"project": project} )

@permission_required('projects_primavera.add_project')
def posting(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        date = request.POST['date']
        new = Project.objects.create(image = image, title = title, description = description, date = date)
        new.save()
        return redirect('projects_primavera:projects')
        
    return render(request, 'project_posting/postingProject.html',{})

def listactivities(request):
    activities = Activities.objects.all()
    return render (request, 'project_posting/listactivities.html', {"activities": activities} )

@permission_required('projects_primavera.add_activities')
def activities(request):
    if request.method == 'POST':
        form = ActivitiesForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('projects_primavera:activities')
    else:
        form = ActivitiesForm()
        return render(request, "project_posting/activities.html", {'form':form}) 
