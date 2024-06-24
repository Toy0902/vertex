from django.contrib import admin
from blog.models import Rasmlar,Matn


# Register your models here.


@admin.register(Rasmlar)
class RasmAdmin(admin.ModelAdmin):
    list_display = ['nomi']


@admin.register(Matn)
class MatnAdmin(admin.ModelAdmin):
    list_display = ['nomi']