from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from .forms import LoginForm
from users.models import User
from _game_chats.mixins import LoginNotRequiredMixin
from .constants import message_user_login_error

class IndexView(TemplateView):
    template_name = "home/index.html"

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

        return redirect(self.success_url)