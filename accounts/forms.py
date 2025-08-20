from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(min_length= 3,  widget=forms.PasswordInput(attrs={'placeholder': "mot de passe"}))