from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=3)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username} ({self.password})"