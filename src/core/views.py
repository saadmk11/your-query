# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from questions.models import Question

# Create your views here.
def home(request):
    queryset = Question.objects.all()[:6]
    context = {"queryset": queryset}
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html", {})