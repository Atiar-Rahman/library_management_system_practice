from django.db import models

# Create your models here.

class Publishers(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return f"publishers {self.name}"
    

