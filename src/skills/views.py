from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Skill
from profiles.models import Profile
from django.views.generic import TemplateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class AllChartView(LoginRequiredMixin, TemplateView):
    template_name = "skills/all_charts.html"

    def get_context_data(self, **kwargs):
        context = super(AllChartView, self).get_context_data(**kwargs)
        qs = Skill.objects.values('name').annotate(total=Sum('score'))
        context["qs"] = qs
        return context


class UserChartView(LoginRequiredMixin, TemplateView):
    template_name = 'skills/user_skills.html'

    def get_object(self):
        pk = self.kwargs.get('profile_id')
        return pk

    def get_context_data(self, **kwargs):
        context = super(UserChartView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(name__id=self.get_object())
        qs = profile.skill_set.all()
        context["qs"] = qs
        return context


@login_required
def skill_view(request):
    user_id = request.user.id
    profile = Profile.objects.get(pk=user_id)

    SkillFormset = inlineformset_factory(
        Profile, Skill, fields='__all__', extra=1, can_delete=True)

    formset = SkillFormset(request.POST or None, instance=profile)
    if formset.is_valid():
        formset.save()

        return redirect('skills:my-skills')

    qs = profile.skill_set.all()

    context = {
        'formset': formset,
        'qs': qs,
    }

    return render(request, 'skills/add.html', context)
