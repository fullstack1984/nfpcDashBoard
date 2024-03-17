from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from mainapp import models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class TablePageView(TemplateView):
    template_name = "mainapp/tables.html"

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context["jk_data_now"] = models.PlanOms.get_values_to_db('jk')
        context["kdo_data_now"] = models.PlanOms.get_values_to_db('kdo')
        return context


class PlanOmsPageView(TemplateView):
    template_name = "mainapp/planOms.html"

    def post(self, request, *args, **kwargs):
        pass


class DataOmsPageView(TemplateView):
    template_name = "mainapp/dataOms.html"

    def post(self, request, *args, **kwargs):
        data_db = models.PlanOms.objects.create(
            name_department='jk',
            values_data=request.POST.get('jk'),
            name_data='dataOms'
        )        
        data_db = models.PlanOms.objects.create(
            name_department='kdo',
            values_data=request.POST.get('kdo'),
            name_data='dataOms'
        )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:dataOms"))