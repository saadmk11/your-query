# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        # return redirect("")
    context = {"form":form,
               "title":title
    }

    return render(request, "accounts/form.html", context)


def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        form.save()
        user = authenticate(email=email, password=password)
        login(request, user)
        # return redirect("create")

    context = {"title":title, "form":form}

    return render(request, "accounts/form.html", context)


def logout_view(request):
    if not request.user.is_authenticated():
        return redirect("login")
    else:
        logout(request)
        return redirect("login")
    