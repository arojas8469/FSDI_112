from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView 
from django.urls import reverse_lazy 

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

# Create your views here.
class PasswordChangeView(PasswordChangeView):
    template_name = "change_password.html" 
    success_url = reverse_lazy("home")  
    
class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "change_password_done"
    success_url = reverse_lazy("home") 