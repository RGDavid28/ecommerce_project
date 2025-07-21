from django import forms

#class SearchForm(forms.Form):
#    q = forms.CharField()

MY_CHOICES =[
    ("db-value1", "Opción 1" ),
    ("o2", "Opción 2"),
    ("o3", "Opción 3")
]    

YEARS = [x for x in range(2023,2030)]

from .models import OwnUser

class ProductModelForm(forms.ModelForm):
    
    class Meta:
        model = OwnUser
        fields = [
            "email",
            "full_name",
            "staff",
            "admin",
        ]
        exclude = []

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        
        if "@" not in email:
            raise forms.ValidationError("El email debe llevar @")    
        return email

    def clean_full_name(self, *args, **kwargs):
        full_name = self.cleaned_data.get("full_name")
        if len(full_name) <= 10:
            raise forms.ValidationError("El Nombre del usuario debe tener mas de 10 caracteres") 
        return full_name
    

class TestForm(forms.Form):
    fecha               = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    un_texto            = forms.CharField(label="Ingrese un texto:", widget=forms.Textarea(attrs={"rows":4,"cols":20}))
    booleano            = forms.BooleanField()
    entero              = forms.IntegerField()
    correo              = forms.EmailField()
    opciones_radio      = forms.CharField(label="seleccione una opción", widget=forms.Select(choices=MY_CHOICES))
    opciones_checkbox   = forms.CharField(label="Selecciona una una opción", widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))
    
    def clean_entero(self, *args, **kwargs):
        entero = self.cleaned_data.get("entero")
        if entero > 100:
            raise forms.ValidationError("El número debe ser menor o igual que 100")
        return entero
     
    def clean_un_texto(self, *args, **kwargs):
        un_texto = self.cleaned_data.get("un_texto")
        if len(un_texto) <10:
            raise forms.ValidationError("El texto debe contener mas de 10 caracters")
        return un_texto