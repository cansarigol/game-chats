from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ManageView(LoginRequiredMixin, TemplateView):
    template_name = "users/manage/user_infos.html"
