from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # Text field with max length
    description = models.TextField(blank=True, null=True)  # Optional text field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field
    stock = models.IntegerField()  # Integer field
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto update timestamp

    def __str__(self):
        return self.name  # Display product name in Django Admin
