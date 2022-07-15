from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404

from admin_dash.models import Question
from .forms import UserForm, LoginForm
from .models import *

# Create your views here.
def index(request):
    return render(request, 'ide/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            question = Question.objects.all()
            stud_email = form.cleaned_data['email']
            stud_pass = form.cleaned_data['password']
            db_stud = Student.objects.filter(email=stud_email, password=stud_pass)
            if not db_stud:
                return HttpResponse("Login failed")
            else:
                request.session['z'] = stud_email
                request.session.get_expiry_age()
                instance = get_object_or_404(Student, email=stud_email)
                return render(request, 'ide/playground.html', {'question': question, 'student': Student.full_name, 'instance': instance})
    else:
        form = LoginForm()
        return render(request, 'ide/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully added')
            return redirect('/login')
    else:
        form = UserForm()
    return render(request, 'ide/signup.html', {'form': form})

def playground(request):
    return render(request, 'ide/playground.html')