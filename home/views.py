from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, FormView, View, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import login

from .forms import LoginForm, SignupForm, ResetForm
from users.models import User, UserProfile
from _game_chats.mixins import LoginNotRequiredMixin
from .constants import message_user_login_error
from game_requests.adapter import BaseAdapter
from tasks.user_queue import send_mail

class IndexView(TemplateView):
    template_name = "home/index.html"

class GamesListView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        order = request.GET.get('order', 'popularity:desc')
        page = request.GET.get('page', 1)
        games_list = []
        if q:
            games_list = BaseAdapter()._games_list_from_name(q, order)
        return render(request, 'home/games_list.html', {
            'games_list': games_list, 
            'q': q, 'page': page, 
            'order': order
        })

class LoginView(LoginNotRequiredMixin, FormView):
    template_name = 'home/login.html'
    success_url = "home:index"
    form_class = LoginForm

    def form_valid(self, form):
        form_clean = form.clean()
        email = str(form_clean['email'])
        password = str(form_clean['password'])
        user = User.objects.get_from_email(email)
        if not user or not user.check_password(password):
            messages.error(self.request, message_user_login_error)
            return render(self.request, self.template_name, {'form': form, })

        login(self.request, user)
        return redirect(self.success_url)

class ResetPasswordView(LoginNotRequiredMixin, FormView):
    template_name = 'home/reset.html'
    success_url = "home:index"
    form_class = ResetForm

    def form_valid(self, form):
        form_clean = form.clean()
        email = str(form_clean['email'])
        user = User.objects.get_from_email(form_clean['email'])
        if not user:
            messages.error(self.request, "E-mail not found!")
            return render(request, 'home/reset.html', {
                'form': form
            })
        new_profile = UserProfile(user=user).update_or_save()
        send_mail.apply_async(
            kwargs={
                'template': "emails/reset_user.html",
                'context': {'domain': settings.DOMAIN,
                            'user': user.name,
                            'activation_key': new_profile.activation_key},
                            'email': [user.email, ],
                            'subject': "Reset your password"
            },
            queue='user_tasks_queue',
            routing_key='emails.user'
        )
        
        messages.success(self.request, "Reset password email has been sent")
        return redirect(self.success_url)


class SignupView(LoginNotRequiredMixin, CreateView):
    template_name = 'home/signup.html'
    success_url = "home:index"
    form_class = SignupForm

    def get_success_url(self):
        newuser = self.object
        newuser.set_password(newuser.password)
        newuser.save()
        new_profile = UserProfile(user=newuser)
        new_profile.save()

        send_mail.apply_async(
                kwargs={
                    'template': "emails/confirm_user.html",
                    'context': {'domain': settings.DOMAIN,
                                'user': newuser.name,
                                'activation_key': new_profile.activation_key},
                                'email': [newuser.email, ],
                                'subject': "Confirm your account"
                },
                queue='user_tasks_queue',
                routing_key='emails.user'
            )
            
        messages.success(self.request, "We've sent your confirmation email!")
        return reverse_lazy(self.success_url)