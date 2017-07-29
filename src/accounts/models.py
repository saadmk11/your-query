# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class User(AbstractUser):
    username = models.CharField(max_length=512, unique=True, blank=False,
                                validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric or contain any of the following: ".+ -" ',
                                        code='invalid_username'
                                        )]
                                )
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=512, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(null=True, 
                                blank=True, 
                                height_field="height_field", 
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
    height_field = models.IntegerField(default=600)
    width_field = models.IntegerField(default=600)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"username": self.username})

    