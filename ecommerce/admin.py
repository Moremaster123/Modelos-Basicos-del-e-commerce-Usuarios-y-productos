from django.contrib import admin

from .models import PerfilUsuario, Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'direccion')
    search_fields = ('usuario__username', 'usuario__email')
