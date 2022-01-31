"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notesapp import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteView, 'notes') # Adds /api/notes path, more below.

urlpatterns = [
    path('admin/', admin.site.urls),

    # Allows creating new Note at localhost:8000/api/notes
    # Query /notes/ returns a list of all Note items, can CREATE and READ there.
    # Query /notes/[id] returns a single Note with that id as its primary key,
    # can UPDATE and DELETE there.
    path('api/', include(router.urls)),
]