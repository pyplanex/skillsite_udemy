from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserChartView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/user_skills.html'

    def get_object(self):
        pk = self.kwargs.get('profile_id')
        return pk

    def get_context_data(self, **kwargs):
        context = super(UserChartView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(name__id=self.get_object())
        qs = profile.skill_set.all()
        context["qs"] = qs
        return context


class UserListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/user_list.html'
