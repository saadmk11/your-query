# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, AnswerForm
from .models import Category, Question, Answer, SendNotification
# Create your views here.


def question_list(request):
    queryset = Question.objects.all()

    query = request.GET.get("q")   
    if query:
        queryset = queryset.filter(
            Q(qus__icontains=query)|
            Q(category__name__icontains=query)
            ).distinct()

    paginator = Paginator(queryset, 12)
    page = request.GET.get("page")
    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)

    context = { "query_list": query_list }
    return render(request, "questions/question_list.html", context)


def question_detail(request, slug=None):
    question = get_object_or_404(Question, slug=slug)
    answers_list = Answer.objects.filter(question=question)
    context = { "question": question,
                "answers_list": answers_list,
                 }
    if request.user.is_authenticated():
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Answer was Posted.')
            form = AnswerForm()    
        context = { "question": question,
                    "form": form,
                    "answers_list": answers_list,
                  }
    return render(request, "questions/question_detail.html", context)


@login_required()
def question_ask(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        messages.success(request, 'Question was Posted.')
        return redirect(question.get_absolute_url())
    context = { "form": form,
                "title": "Ask Question"
              }
    return render(request, "questions/ask.html", context)


@login_required()
def question_update(request, slug=None):
    instance = get_object_or_404(Question, slug=slug)
    if instance.user != request.user:
        raise Http404
    else:
        form = QuestionForm(request.POST or None, instance=instance)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, 'Question was Updated.')
            return redirect(question.get_absolute_url())
        context = { "form": form,
                    "title": "Edit Question"
                    }
    return render(request, "questions/ask.html", context)


@login_required()
def question_delete(request, slug=None):
    question = get_object_or_404(Question, slug=slug)
    if not request.user.is_authenticated():
        raise Http404 
    else:
        if question.user != request.user:
            raise Http404
        else:
            question.delete() 
            messages.error(request, 'Question was Deleted.')
            return redirect(request.user.get_absolute_url()) 


@login_required()
def answer_update(request, slug=None, pk=None):
    question = get_object_or_404(Question, slug=slug)
    instance = get_object_or_404(Answer, pk=pk)
    if instance.user != request.user:
        raise Http404
    else:
        form = AnswerForm(request.POST or None, instance=instance)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Answer was Updated.')
            return redirect(question.get_absolute_url())
        context = { "form": form,
                    "title": "Update Answer"
                    }
    return render(request, "questions/answer.html", context)


@login_required()
def answer_delete(request, slug=None, pk=None):
    question = get_object_or_404(Question, slug=slug)
    answer = get_object_or_404(Answer, pk=pk)
    if not request.user.is_authenticated():
        raise Http404 
    else:
        if answer.user != request.user:
            raise Http404
        else:
            answer.delete() 
            messages.error(request, 'Answer was Deleted.')
            return redirect(question.get_absolute_url())


def category_list(request):
    categories = Category.objects.all()
    context = { "categories": categories }
    return render(request, "questions/category_list.html", context)


def category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)   
    queryset = category.question_set.all()

    query = request.GET.get("q")   
    if query:
        queryset = queryset.filter(
            Q(qus__icontains=query)
            ).distinct()

    paginator = Paginator(queryset, 12)
    page = request.GET.get("page")
    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)
        
    context = { "query_list": query_list,
                "category": category
              }
    return render(request, "questions/category.html", context)


@login_required()
def notification(request):
    user = request.user
    notification = SendNotification.objects.filter(user=user)
    notification.update(viewed=True)

    paginator = Paginator(notification, 12)
    page = request.GET.get("page")
    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)

    context = { "query_list": query_list }
    return render(request, "questions/notification.html", context)
