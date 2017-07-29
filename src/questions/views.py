# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Category, Question, Answer
# Create your views here.
def question_list(request):
    queryset = Question.objects.all()
    context = { "queryset": queryset }
    return render(request, "questions/question_list.html", context)


def question_detail(request, pk=None):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question)
    context = { "question": question,
                "answers": answers,
                 }
    return render(request, "questions/question_detail.html", context)


def category_list(request):
    categories = Category.objects.all()
    context = { "categories": categories }
    return render(request, "questions/category_list.html", context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)   
    queryset = category.question_set.all()
    context = { "queryset": queryset }
    return render(request, "questions/category.html", context)