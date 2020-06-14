from django.contrib import admin
from .models import Technician, MassageItem


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'avatar', 'gender', 'type', )


@admin.register(MassageItem)
class MassageItemAdmin(admin.ModelAdmin):
    list_per_page = 20
