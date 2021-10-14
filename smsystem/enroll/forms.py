from django import forms
from django.forms import widgets
from enroll.models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['rollno', 'name', 'email', 'password']
        widgets = {
            'rollno' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
