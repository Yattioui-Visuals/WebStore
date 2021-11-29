from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Products, Customer, Orders
from .permissions import IsAdminUserOrReadOnly, IsAdminUserOrOwner, IsAdminUserOrOwnerOrder
from .serializers import ProductsSerializer, CustomerSerializer, OrdersSerializer

"""
I had not worked with the Django Rest Framework before, so when I saw the assignment I started reading the doc, and 
following along with some tutorial to get the hang of it. So i didn't get complete it as fully as I wanted to
but I really enjoyed learning the framework and defintely will keep expanding on this project :)
"""


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
        # Trying to give the stock some logic so the orders would get handled as intended

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders
    serializer_class = OrdersSerializer

    permission_classes = [IsAdminUserOrOwnerOrder]
