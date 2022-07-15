from django import forms
from .models import Student

class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {'full_name', 'email', 'password'}
        labels = {'full_name': 'Name', 'email': 'email', 'password': 'password'}
        widgets = {'password': forms.PasswordInput()}
    def validate_email(self):
        email = self.cleaned_data.get('email')
        stud_qs = Student.objects.filter(email=email)
        if stud_qs.exists():
            raise forms.ValidationError("User already Exists")
        return email


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

