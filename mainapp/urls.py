from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name='main_page'),
    path("tables/", views.TablePageView.as_view(), name='tables'),
    path("planOms/", views.PlanOmsPageView.as_view(), name='planOms'),
    path('dataOms/', views.DataOmsPageView.as_view(), name='dataOms'),
]