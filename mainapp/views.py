from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from mainapp import models
from mainapp.utils import matplo_data


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class TablePageView(TemplateView):
    """
    Обработчик формирует таблицу 
    """
    template_name = "mainapp/tables.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']

        for item in list_otd:
            # ОМС
            context[f"{item}_data_now"] = models.ModelOms.get_values_to_db_data(item)
            # Платные услуги 
            context[f"{item}_data_plat"] = models.ModelPlat.get_values_to_db_data(item)
            # ВМП
            context[f"{item}_data_vmp"] = models.ModelVmp.get_values_to_db_data(item)
            context[f"{item}_data_vipis"] = models.ModelVipis.get_values_to_db_data(item)
            context[f"{item}_plan_vipis"] = models.ModelVipis.get_values_to_db_data(item, 'planVipis')
            context[f"{item}_res_vipis"] = models.ModelVipis.get_values_to_db_data(item) + models.ModelVipis.get_values_to_db_data(item, 'planVipis')
        
        return context


class PlanOmsPageView(TemplateView):
    """
    Обработчик формы для плановых показателей по ОМС
    """
    template_name = "mainapp/planOms.html"

    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']

        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelOms.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelOms.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()        
        return HttpResponseRedirect(reverse_lazy("mainapp:planOms"))


class DataOmsPageView(TemplateView):
    """
    Обработчик формы фактическим показателям ОМС
    """

    template_name = "mainapp/dataOms.html"

    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelOms.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelOms.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:dataOms"))
    

class PlanPlatPageView(TemplateView):
    """
    Обработчик формы плановых показателей по платным услугам 
    """

    template_name = "mainapp/planPlat.html"

    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelPlat.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelPlat.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:planPlat"))


class DataPlatPageView(TemplateView):
    """
    Обработчик формы фактическим показателям платных услуг
    """
    template_name = "mainapp/dataPlat.html"

    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelPlat.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelPlat.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:dataPlat"))

class DataVmpPageView(TemplateView):
    """
    Обработчик формы фактическим показателям ВМП
    """

    template_name = "mainapp/dataVmp.html"
    
    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelVmp.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelVmp.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:dataVmp"))


class PlanVmpPageView(TemplateView):
    """
    Обработчик формы плановых показателей по ВМП
    """
    template_name = "mainapp/planVmp.html"
    
    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelVmp.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelVmp.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:planVmp"))


class PlanVipisPageView(TemplateView):
    """
    Обработчик формы плановых показателей по Архив 
    """
    template_name = "mainapp/planVipis.html"
    
    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelVipis.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelVipis.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:planVipis"))


class DataVipisPageView(TemplateView):
    """
    Обработчик формы фактическим показателям Архив
    """

    template_name = "mainapp/dataVipis.html"
    
    def post(self, request, *args, **kwargs):
        list_otd = ['kdo', 'jk', 'dsr_w', 'katamnez', 'dsr_ch', 'ot_fu_di', 'olmrd', 'vrt', 'prim_otd', 'aopb_1', 'aopb_2', 'rod_otd', 'rod_otd_1', 'afonion', 'oar', 'oritn', 'opnd', 'rkc', 'go', 'kdl']       
        
        for item in list_otd:
            if request.POST.get(item) is not None:
                data_db = models.ModelVipis.objects.create(
                    name_department=item,             
                    values_data=request.POST.get(item),
                    name_data=request.path.split('/')[2]
                )
            else:
                data_db = models.ModelVipis.objects.create(
                    name_department=item,             
                    values_data=0,
                    name_data=request.path.split('/')[2]
                )
        data_db.save()
        return HttpResponseRedirect(reverse_lazy("mainapp:dataVipis"))