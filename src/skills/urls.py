from django.urls import path
from .views import skill_view, UserChartView, AllChartView

app_name = 'skills'

urlpatterns = [
    path('', skill_view, name='my-skills'),
    path('all/', AllChartView.as_view(), name='all-skills'),
    path('<profile_id>/', UserChartView.as_view(), name='user-skills'),
]
