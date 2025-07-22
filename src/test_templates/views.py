from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib import messages 

#def test_view(request):
def home(request):
    my_list = ["Mouse", "LapTop", "Teclado", "Audio","Celular","Iphone"]
    context = {
        "view_title":"INVENTARIO DE PRODUCTO TERMINADO",
        "my_number" : 3131,
        "my_number2": 2000,
        "today": datetime.now().today(),
        "my_list":my_list
    }
#    template = "test_templates/object-detail.html"  
#   template = "test_templates/test-view.html"
    template = "test_templates/test-view2.html"
    messages.add_message(request, messages.INFO,'Este es un Mensaje de Prueba 1')
    messages.add_message(request, messages.INFO,'Este es otro Mensaje de Prueba 2')
    return render(request, template, context) 