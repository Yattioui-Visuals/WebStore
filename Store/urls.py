from django.urls import path, include

from .views import ProductList, ProductDetail, CustomerList, CustomerDetail, OrderList, OrderDetail, CustomerCreate, \
    OrderCreate

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('api/products', ProductList.as_view(), name='products'),
    path('api/product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail'),

    path('api/customer', CustomerList.as_view(), name='customer'),
    path('api/customer-create', CustomerCreate.as_view(), name='customer-create'),
    path('api/customer-detail/<int:pk>', CustomerDetail.as_view(), name='customer-detail'),

    path('api/orders', OrderList.as_view(), name='orders'),
    path('api/order-create', OrderCreate.as_view(), name='order-create'),
    path('api/order-detail/<int:pk>', OrderDetail.as_view(), name='order-detail'),
]
