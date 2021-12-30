from django.contrib import admin
from django.db import models
from .models import Pizza, Ingrediente, Ingredientes_x_pizza

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Ingredientes_x_pizza)