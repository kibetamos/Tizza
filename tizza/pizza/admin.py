from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pizza
class PizzaAdmin(admin.ModelAdmin):
 pass
admin.site.register(Pizza, PizzaAdmin)