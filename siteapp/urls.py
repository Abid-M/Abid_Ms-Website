from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-skills/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("projects/", views.projects, name="projects"),
]