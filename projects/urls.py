from django.urls import path
from . import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import home, project, projects, post

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', home, name="home"), 
    path('project/<slug>/', post, name="project"),
    path('projects', projects, name="projects"), 
     
]

