from django.contrib import admin

# Register your models here.
from .models import Banner, Producto, Galeria

admin.site.register(Banner)
admin.site.register(Producto)
admin.site.register(Galeria)