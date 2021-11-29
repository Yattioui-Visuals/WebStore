from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Products, Customer, Orders
from .permissions import IsAdminUserOrReadOnly, IsAdminUserOrOwner, IsAdminUserOrOwnerOrder
from .serializers import ProductsSerializer, CustomerSerializer, OrdersSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    permission_classes = [IsAdminUserOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products
    serializer_class = ProductsSerializer

    permission_classes = [IsAdminUserOrReadOnly]


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [permissions.IsAdminUser]


class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer
    serializer_class = CustomerSerializer

    permission_classes = [IsAdminUserOrOwner]


class OrderList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    permission_classes = [permissions.IsAdminUser]


class OrderCreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(self.queryset)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Products.objects.get(product_name=validated_data['product']).stock -= 1

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders
    serializer_class = OrdersSerializer

    permission_classes = [IsAdminUserOrOwnerOrder]
