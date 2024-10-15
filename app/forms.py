from django import forms
from django.forms import Form
from django.forms import ModelForm

from app.models import User
from app.models import Blog


class Registration_From(ModelForm):

    class Meta:

        model=User

        fields=['username','email','password']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control',
                                              'placeholder': 'Enter your username . . .'}),

            'email':forms.TextInput(attrs={'class':'form-control',
                                            'placeholder': 'Enter your email . . .'}),

            'password':forms.PasswordInput(attrs={'class':'form-control',
                                                  'placeholder': 'Enter password . . .'})
        }


class Blog_Form(ModelForm):

    class Meta:

        model=Blog

        fields=['title','content']

        read_only_fields=['user','created_date','updated_date']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control',
                                              'placeholder': 'Write the heading . . .'}),

            'content': forms.Textarea(attrs={'class': 'form-control', 
                                                 'placeholder': 'Write content . . .'})
        }


class Login_Form(forms.Form):

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',
                                                                            'placeholder':'Username . . .'}))
    
    password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',
                                                                           'placeholder':'password . . .'}))


