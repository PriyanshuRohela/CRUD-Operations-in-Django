from django.db import models

# Create your models here.

class entries(models.Model):
    username = models.CharField(max_length=20)
    passwordd = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    