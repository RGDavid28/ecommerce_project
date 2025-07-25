from django.shortcuts   import  render
from rest_framework     import  generics
from .pagination        import  ProductPagination, ProductLOPagination, ProductCPagination
from .serializers       import  ProductSerializer
from .models            import Product

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#    pagination_class = ProductPagination
#    pagination_class = ProductLOPagination
    pagination_class = ProductCPagination