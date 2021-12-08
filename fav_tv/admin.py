from django.contrib import admin
from .models import FavTv


@admin.register(FavTv)
class AdminFav(admin.ModelAdmin):
    list_display = ["name" , "sort"]

