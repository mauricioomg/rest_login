from django import forms

class  UserForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class  ProductForm(forms.Form):
    fullname = forms.CharField(required=True)
    price = forms.EmailField(required=True)
    detail = forms.CharField(required=True)

