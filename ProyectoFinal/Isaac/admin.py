from django.contrib import admin
from .models import Item, Objeto, Usuario

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'precio')
    list_display = ('id', 'nombre', 'precio')

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'precio')
    list_display = ('id', 'nombre', 'precio')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'email')
    list_display = ('id', 'nombre', 'email')




#admin.site.register(Item, ItemAdmin)
#admin.site.register(Objeto)
#admin.site.register(Usuario)