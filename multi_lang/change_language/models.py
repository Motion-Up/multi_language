from parler.models import TranslatableModel, TranslatedFields

from django.db import models


class Example(TranslatableModel):
    translations = TranslatedFields(
        text=models.TextField(
            "Текст",
            max_length=200,
        ),
    )

    def __unicode__(self):
        return self.title
