# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, AnswerForm
from .models import Category, Question, Answer
# Create your views here.

def question_list(request):
    queryset = Question.objects.all()
    context = { "queryset": queryset }
    return render(request, "questions/question_list.html", context)


def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
        form = AnswerForm()
    answers_list = Answer.objects.filter(question=question)
    context = { "question": question,
                "form": form,
                "answers_list": answers_list,
                 }
    return render(request, "questions/question_detail.html", context)


def question_ask(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        return redirect(question.get_absolute_url())
    context = { "form": form,
                "title": "ask"
                 }
    return render(request, "questions/ask.html", context)


def category_list(request):
    categories = Category.objects.all()
    context = { "categories": categories }
    return render(request, "questions/category_list.html", context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)   
    queryset = category.question_set.all()
    context = { "queryset": queryset }
    return render(request, "questions/category.html", context)