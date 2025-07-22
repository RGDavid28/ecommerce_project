from rest_framework import views
from rest_framework.response import Response

# Create your views here.
class ProductAPIView(views.APIView):

    def get(self, request):
        content = {
            "Estas llmando el método GET"
        }
        return Response(content)
    
    def post(self, request):
        content = {
            "Estas llmando el método POST"
        }
        return Response(content)
    
    def patch(self, request):
        content = {
            "Estas llmando el método PATCH"
        }
        return Response(content)
    
    def delete(self, request):
        content = {
            "Estas llmando el método DELETE"
        }
        return Response(content)