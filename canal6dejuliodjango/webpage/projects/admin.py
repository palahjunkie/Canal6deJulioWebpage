from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Project, Review, Tag, Entrada, Contacto

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )
    
class EntradaAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Contacto)