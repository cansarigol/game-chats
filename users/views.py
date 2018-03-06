from django.views.generic import TemplateView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from users.models import UserProfile
from .forms import ChangePasswordForm

class ManageView(LoginRequiredMixin, TemplateView):
    template_name = "users/manage.html"

class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/change_password.html'
    success_url = 'home:index'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        form_clean = form.clean()
        password = form_clean['password']
        user = self.request.user
        user.set_password(password)
        user.save()
        login(self.request, user)
        return redirect(self.success_url)


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('home:index')

def valid_user(request, activation_key):
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
    user = user_profile.user
    user.is_active = True
    user.save()

    login(request, user)
    messages.success(request, "Your account has been activated successfully")
    return redirect('home:index')

def valid_reset_password(request, activation_key):
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
    user = user_profile.user
    if not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated successfully")

    login(request, user)
    
    return redirect('users:change_password')