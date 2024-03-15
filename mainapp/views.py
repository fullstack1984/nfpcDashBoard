from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class TablePageView(TemplateView):
    template_name = "mainapp/tables.html"


class PlanOmsPageView(TemplateView):
    template_name = "mainapp/planOms.html"

    def post(self, request, *args, **kwargs):
        pass
