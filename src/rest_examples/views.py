from rest_framework import viewsets
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer

      def list(self, request):
            products = self.get_queryset()
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)

      def retrieve(self, request, pk=None):
            product = self.get_object()
            serializer = self.get_serializer(product)
            return Response(serializer.data)

      def update(self, request, pk=None):
            product = self.get_object()
            serializer = self.get_serializer(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)