from django.shortcuts import render ,redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm
# Create your views here.
def loginView(request):
    next = request.GET.get("next")
    title ="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request ,user)
        if next:
            return redirect(next)
        else:
            return redirect("/")
    return render(request,"new_app/form.html",{"form":form,"title" : title})

def logoutView(request):
    logout(request)
    return redirect("/")

def registerView(request):
    next = request.GET.get("next")
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        if next:
            return redirect(next)
        else:
            return redirect("/")
    return render(request,"new_app/form1.html",{'form' : form , 'title': title})
