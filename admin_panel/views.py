from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product
from .forms import ProductForm

# View to list all products
@staff_member_required
def product_list(request):
    # products = Product.objects.all()
    return render(request, 'index.html')

# # View to add a new product
# @staff_member_required
# def product_add(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'product_add.html', {'form': form})

# # View to edit a product
# @staff_member_required
# def product_edit(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'product_edit.html', {'form': form})

# # View to delete a product
# @staff_member_required
# def product_delete(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'product_confirm_delete.html', {'product': product})
