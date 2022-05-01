from pyexpat import model
from django.db import models


class Example(models.Model):
    text = models.TextField("Текст", max_length=200)
