from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.pk = 1
        return super().save(*args, **kwargs)

    @classmethod
    def save_company(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    @classmethod
    def get_company(cls):
        try:
            obj = cls.objects.get(pk=1)
            return obj
        except cls.DoesNotExist:
            return
