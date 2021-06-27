from  django import forms
from django.contrib.auth.models import User

class Userloginform(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'your username'}))
    password= forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder':'your password'}))
class Userregisterform(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'your username'}))
    emailadress= forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'your emailaderss'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'your password'}))
    def chean_emailadress(self):
        emailadress = self.cleaned_data['emailadress']
        user = User.objects.filter(emailadress=emailadress)
        if user.exists():
            raise forms.ValidationError('This email already exists')
        return emailadress