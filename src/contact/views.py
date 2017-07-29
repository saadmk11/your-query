# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        contact_email = form.cleaned_data['contact_email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, contact_email, ['admin@hotmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')
    context = {"form": form}
    return render(request, "contact/contact.html", context)
