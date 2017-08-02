from django import forms
from .models import Question, Answer



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["qus", "details", "category"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["ans"]

