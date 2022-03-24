from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome_comentario', 'email_comentario',
                    'data_comentario', 'id', 'publicado_comentario',)
    list_editable = ('publicado_comentario', )
    list_display_link = ('id', 'nome_comentario', 'email_comentario',)


admin.site.register(Comentario, ComentarioAdmin) 