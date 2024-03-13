from django.db import models


class PlanOms(models.Model):
    name_department = models.CharField(max_length=256, verbose_name='NameDepartmetn')

    values_data = models.PositiveIntegerField(blank=True, null=True,verbose_name='ValuesData')

    plan_data = models.PositiveIntegerField(blank=True, null=True,verbose_name='PlanData')

    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    date_update = models.DateTimeField(auto_now=True, verbose_name="Edited")

    deleted = models.BooleanField(default=False)
