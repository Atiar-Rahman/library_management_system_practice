from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"auher name is {self.name}"
