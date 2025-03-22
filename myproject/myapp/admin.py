from django.contrib import admin
from myapp.models import Product

# Register your models here.
@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display=("name","description","stock","price","created_at")

    search_fields = ("name",)
    