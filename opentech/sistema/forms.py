from django import forms

class formcadastro(forms.Form):
    nome = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(widget=forms.PasswordInput)