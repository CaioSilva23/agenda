from django.contrib import admin
from .models import Categoria, Contato



class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone','date_created',\
                     'email', 'categoria')
    list_display_links = ('id','nome', 'sobrenome')
    #list_editable = ('nome', 'sobrenome')
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)