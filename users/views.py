from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from users.models import UserProfile

class ManageView(LoginRequiredMixin, TemplateView):
    template_name = "users/manage.html"


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