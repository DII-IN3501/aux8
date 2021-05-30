from django import forms

class Formulario(forms.Form):
    fname = forms.CharField(label='Primer Nombre')
    lname = forms.CharField(label='Segundo Nombre')

    need1 = forms.BooleanField(label="Tengo sueño", required=False)
    need2 = forms.BooleanField(label="Tengo hambre", required=False)
    need3 = forms.BooleanField(label="Tengo pena", required=False)

    CHOICES = (('si1', "Sí"),
               ('si2', "Sí, pero con choreza"))
    nota = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
