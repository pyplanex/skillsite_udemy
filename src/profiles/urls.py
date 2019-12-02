from django.urls import path
from .views import UserListView, UserChartView

app_name = 'profiles'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<profile_id>/', UserChartView.as_view(), name='user-chart'),
]
