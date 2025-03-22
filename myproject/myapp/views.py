from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        product = Product(name=name,description=description,price=price,stock=stock)
        product.save()

        return redirect('home')
    return render(request, 'about.html')

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        # Update product fields
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock
        product.save()
        
        return HttpResponse(f"Product {product.name} updated successfully!")
    
    return render(request, 'update_product.html', {'product': product})