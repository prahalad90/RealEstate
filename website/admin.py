from django.contrib import admin
from .models import property,agent,blog, images

# Register your models here.
@admin.register(property)
class propertyAdmin(admin.ModelAdmin):
    list_display = ['name','price','stat']

@admin.register(agent)
class agentAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['title','date']

@admin.register(images)
class imageAdmin(admin.ModelAdmin):
    list_display = ['listing','image']