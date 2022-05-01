from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Example


#class ExampleAdmin(admin.ModelAdmin):
#    list_display = ('text',)
#
#
#admin.site.register(Example, ExampleAdmin)


class ExampleAdmin(TranslationAdmin):
    list_display = ('text',)
    search_fields = ('text',)


admin.site.register(Example, ExampleAdmin)
