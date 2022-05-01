from modeltranslation.translator import (
    register, TranslationOptions, translator)


from .models import Example


class ExampleTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('ru', 'en')


translator.register(Example, ExampleTranslationOptions)
