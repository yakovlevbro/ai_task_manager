from django.urls import path
from .views import AddProjectView, CreateGanttView

urlpatterns = [
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    path('create_gantt/', CreateGanttView.as_view(), name='create_gantt'),
]
