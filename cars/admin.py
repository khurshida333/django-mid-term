from django.contrib import admin
from . import models
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display  =  ['name','slug']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'car', 'created_on']
    search_fields = ['name', 'car__name']


admin.site.register(models.Car,CarAdmin)
admin.site.register(models.Comment,CommentAdmin)