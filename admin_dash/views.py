from django.shortcuts import render
from .forms import LecForm
from django.contrib import messages


# Create your views here.
def index(request):
    pass

def login(request):
    return render(request, 'admin_dash/login.html')

def signup(request):
    if request.method == 'POST':
        form = LecForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully added')
            return login(request)
    else:
        form = LecForm()
    return render(request, 'admin_dash/lec_signup.html', {'form': form})
