from django.urls import path
from main.views import HomePlumbing, HomeElectricity, WorkPlumbing, WorkElectricity

urlpatterns = [
    path('', HomePlumbing.as_view(), name='main_plumbing'),
    path('electricity/', HomeElectricity.as_view(), name='main_electricity'),
    path('work-plumbing/', WorkPlumbing.as_view(), name='work_plumbing'),
    path('work-electricity/', WorkElectricity.as_view(), name='work_electricity'),
]