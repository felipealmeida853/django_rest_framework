from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False, blank=True, null=True)
    erro = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title
