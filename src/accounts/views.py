from django.shortcuts import render, redirect

#from .forms import SearchForm ----> Ejercicio 1
from .forms import TestForm, ProductModelForm
#, UserModelForm

def home(request):
#    form = SearchForm()    ----> Ejercicio 1
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/forms')
    return render(request, "forms.html",{"form":form})

#   form = TestForm(request.POST or None, initial=initial_data)
#    if form.is_valid():
#        print(form.cleaned_data)
#    return render(request, "forms.html", {"form":form})