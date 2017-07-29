# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    )
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm
from .models import User

# Create your views here.
def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect("home")
    context = {"form":form,
               "title":title
    }

    return render(request, "accounts/form.html", context)


def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        new_user = authenticate(email=user.email, password=password)
        login(request, new_user)
        return redirect("home")

    context = {"title":title, "form":form}

    return render(request, "accounts/form.html", context)


def logout_view(request):
    if not request.user.is_authenticated():
        return redirect("login")
    else:
        logout(request)
        return redirect("home")


def user_profile(request, username=None):
    user_profile = get_object_or_404(User, username=username)
    context = { "user_profile": user_profile }
    return render(request, "accounts/profile.html", context)

