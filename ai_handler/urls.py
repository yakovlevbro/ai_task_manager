from django.urls import path
from .views import AddProjectView

urlpatterns = [
    path('add_project/', AddProjectView.as_view(), name='add_project'),
]
