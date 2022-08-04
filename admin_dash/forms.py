from django import forms
from .models import Lecturer

class LecForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = {'lec_name', 'admin_email', 'admin_password', 'lec_department'}
        labels = {'lec_name': 'Name', 'admin_email': 'email', 'admin_password': 'password', 'lec_daprtment': 'Department'}
        widgets = {'admin_password': forms.PasswordInput()}
    
    def validate_email(self):
        email = self.cleaned_data.get('admin_email')
        lec_qs = Lecturer.objects.filter(email=email)
        if lec_qs.exists():
            raise forms.ValidationError("User already Exists")
        return email