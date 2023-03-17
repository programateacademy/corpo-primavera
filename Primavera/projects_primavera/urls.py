from django.urls import path
from .views import render_projects, project_detail
from . import views

app_name = "projects_primavera"

urlpatterns = [
    path("", render_projects, name = "projects"),
    path("<int:project_id>", project_detail, name ="project_detail"),
    path('postingProject',views.posting, name='postingProject'),
    ]