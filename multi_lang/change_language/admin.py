from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Example


admin.site.register(Example, TranslatableAdmin)
