from django.db import models
from common.common import get_file_path


class Technician(models.Model):
    id = models.BigAutoField(u'id', primary_key=True, )
    name = models.CharField(u'技师名称', max_length=20, null=False, blank=False, )
    avatar = models.ImageField(u'头像', upload_to=get_file_path, max_length=100, null=False, blank=False, )
    GENDER_CHOICES = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    gender = models.PositiveSmallIntegerField(u'性别', choices=GENDER_CHOICES, default=2, null=False, blank=False, )
    TYPE_CHOICES = (
        (1, '高级按摩师'),
    )
    type = models.PositiveSmallIntegerField(u'技师类型', choices=TYPE_CHOICES, null=False, blank=False, )

    class Meta:
        db_table = 'uac_technician'
        verbose_name = verbose_name_plural = (u'技师信息管理')

    def __str__(self):
        return self.name


class MassageItem(models.Model):
    id = models.BigAutoField(u'id', primary_key=True, )
    name = models.CharField(u'项目名称', max_length=50, null=False, blank=False, )
    price = models.DecimalField(u'价位', max_digits=6, decimal_places=2, null=False, blank=False, )
    unit = models.CharField(u'单位', max_length=10, null=False, blank=False, )
    duration = models.IntegerField(u'时长', null=False, blank=False, )

    class Meta:
        db_table = 'uac_massage_item'
        verbose_name = verbose_name_plural = (u'项目管理')

    def __str__(self):
        return self.name
