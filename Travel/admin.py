from django.contrib import admin

from .models import Destination,save_destination

@admin.register(Destination)
class Destination(admin.ModelAdmin):
    list_display = ['id']
@admin.register(save_destination)
class save_destinationAdmin(admin.ModelAdmin):
    list_display = ['id']
