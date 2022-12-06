from django import forms

class PersonForm(forms.Form):

    options = [
        ("M", "Masculino"),
        ("F", " Femenino"),
        ("O", "Otros")
    ]

    name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    address_2  = forms.CharField(max_length=200)
    reference = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.PasswordInput()
    phone_number = forms.CharField(max_length=15)
    username = forms.CharField(max_length=60)
    gender = forms.ChoiceField(choices=options)
