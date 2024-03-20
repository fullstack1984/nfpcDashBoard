from django.db import models
from datetime import date, datetime


class ModelOms(models.Model):
    name_department = models.CharField(max_length=256, verbose_name='NameDepartmetn')

    values_data = models.PositiveIntegerField(blank=True, null=True,verbose_name='ValuesData')

    name_data = models.CharField(max_length=256, verbose_name='NameData')

    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    date_update = models.DateTimeField(auto_now=True, verbose_name="Edited")

    deleted = models.BooleanField(default=False)


    @staticmethod
    def get_values_to_db_data(name_dep, name_dat='dataOms'):
        my_data = ModelOms.objects.filter(name_department=name_dep)
        my_list = []
        for i in my_data:
            if i.date_create.strftime('%m/%d/%Y') == date.today().strftime('%m/%d/%Y') and i.name_data == name_dat:                
                my_list.append(i.values_data)
        return my_list[len(my_list) - 1]


class ModelPlat(models.Model):
    name_department = models.CharField(max_length=256, verbose_name='NameDepartmetn')

    values_data = models.PositiveIntegerField(blank=True, null=True,verbose_name='ValuesData')

    name_data = models.CharField(max_length=256, verbose_name='NameData')

    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    date_update = models.DateTimeField(auto_now=True, verbose_name="Edited")

    deleted = models.BooleanField(default=False)


    @staticmethod
    def get_values_to_db_data(name_dep, name_dat='dataPlat'):
        my_data = ModelPlat.objects.filter(name_department=name_dep)
        my_list = []
        for i in my_data:
            if i.date_create.strftime('%m/%d/%Y') == date.today().strftime('%m/%d/%Y') and i.name_data == name_dat:                
                my_list.append(i.values_data)
        return my_list[len(my_list) - 1]