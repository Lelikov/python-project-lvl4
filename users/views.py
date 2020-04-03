from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.views.generic.edit import CreateView

from users.forms import LoginForm, SignUpForm


class SignupUser(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('TaskViews')

    def form_valid(self, form):
        form.save()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('TaskViews'))

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('TaskViews'))
        return super().dispatch(*args, **kwargs)


class LoginUser(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('TaskViews')
    template_name = 'task_manager/main.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginUser, self).form_valid(form)


class LogoutUser(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('Main')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)
