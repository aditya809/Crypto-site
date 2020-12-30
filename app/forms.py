from django import forms
from app.models import reg

class reg_form(forms.Form):
    name=forms.CharField()
    gender=forms.CharField()
    email_reg=forms.EmailField()
    username_reg=forms.CharField()
    password_reg=forms.CharField()

    
