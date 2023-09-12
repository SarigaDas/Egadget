from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic import View,FormView,CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class HomeView(FormView):
    template_name="Mhome.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Success!")
                return redirect('custhome')
            else:
                messages.error(request,"Sign in failed!")
                return redirect('h')
        return render(request,"Mhome.html",{"form":form_data})

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')

    def form_valid(self,form):
        messages.success(self.request,"Registered Successfully!")
        return super().form_valid(form)


class LgoutView(View):
    def get(self,request):
        logout(request)
        return redirect("h")
