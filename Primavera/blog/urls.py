
from django.urls import path
from .views import render_posts, post_detail
from . import views

app_name = "blog"

urlpatterns = [
    path("", render_posts, name = "posts"),
    path("<int:post_id>", post_detail, name ="post_detail"),
    path('posting/', views.posting,name="posting")
    ]