# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="category")
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("questions:category", kwargs={"slug": self.slug})


class Question(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    qus = models.CharField(max_length=256, verbose_name="question")
    details = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.qus

    def _get_unique_slug(self):
        slug = slugify(self.qus)
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    ans = models.TextField(verbose_name="answer")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question.qus

