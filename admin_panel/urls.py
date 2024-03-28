from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_list, name='product_list'),
    # path('product/add/', views.product_add, name='product_add'),
    # path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    # path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
