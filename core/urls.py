from django.urls import path
from .views import CustomLoginView, SignUpView, MainView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', MainView.as_view(), name='main'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
