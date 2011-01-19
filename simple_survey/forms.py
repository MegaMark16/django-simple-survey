from django import forms
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.forms.models import modelformset_factory

from models import Survey, Question, Response, Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['survey','response',]

def get_answer_formset(questions):
    AnswerFormset = modelformset_factory(Answer, form=AnswerForm, can_delete=False, extra=len(questions))
    return AnswerFormset

