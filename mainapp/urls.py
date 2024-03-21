from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name='main_page'),
    path("tables/", views.TablePageView.as_view(), name='tables'),
    path("planOms/", views.PlanOmsPageView.as_view(), name='planOms'),
    path('dataOms/', views.DataOmsPageView.as_view(), name='dataOms'),
    path("dataPlat/", views.DataPlatPageView.as_view(), name='dataPlat'),
    path("planPlat/", views.PlanPlatPageView.as_view(), name='planPlat'),
    path("dataVmp/", views.DataVmpPageView.as_view(), name='dataVmp'),
    path("planVmp/", views.PlanVmpPageView.as_view(), name='planVmp'),
]