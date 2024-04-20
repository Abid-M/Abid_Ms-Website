from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-skills/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("projects/", views.projects, name="projects"),
    path("career-blog/", views.careerblog, name ="career-blog"),
    path("contact/", views.contact, name="contact"),
]