from django.db import models
from publishers.models import Publishers

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Category: {self.name}'


class Books(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)  # Typo fixed from `update_at`
    quantity = models.PositiveIntegerField(default=1)  # Fixed type
    image = models.ImageField(upload_to='books/images/', blank=True, null=True)

    def __str__(self):
        return self.title
