from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.urls import reverse_lazy


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Вы успешно вошли в систему"

    def get_success_url(self):
        return reverse_lazy('main')


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = "Аккаунт успешно создан. Пожалуйста, войдите."

    def form_valid(self, form):
        result = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Аккаунт {username} успешно создан. Пожалуйста, войдите.')
        return result


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'
    login_url = 'login'


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.next_page = reverse_lazy('login')
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
