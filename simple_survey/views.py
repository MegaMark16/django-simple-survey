from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django import forms
from django.contrib.auth.decorators import login_required

from models import Survey, Answer, Response
from forms import get_answer_formset

def list_surveys(request):
    surveys = Survey.objects.all()
    
    responseParameters = {
        "surveys" : surveys,
    }
    return render_to_response('simple_survey/list_surveys.html', responseParameters, context_instance=RequestContext(request))


@login_required()
def take_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.question_set.all()
    AnswerFormset = get_answer_formset(questions)

    formset = AnswerFormset(request.POST or None, queryset=Answer.objects.none())
    if formset.is_valid():
        answers = formset.save(commit=False)
        response = Response(survey=survey)
        response.save()
        for answer in answers:
            answer.response = response
            answer.save()    
        return HttpResponseRedirect(reverse('simple_survey.views.list_surveys'))
        
    for index in range(len(questions)):
        question = questions[index]
        form = formset.forms[index]
        form.fields['answer'].label = question.question
        form.fields['question'].initial = question
        
    responseParameters = {
        "survey" : survey,
        "formset" : formset,
    }
    return render_to_response('simple_survey/take_survey.html', responseParameters, context_instance=RequestContext(request))


