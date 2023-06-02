from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style': 'box-shadow: none'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1"]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        del self.fields['password2']

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'box-shadow: none'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['style'] = 'box-shadow: none'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style': 'box-shadow: none'}))
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'box-shadow: none'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'box-shadow: none'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'box-shadow: none'}))
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email"]