from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

def index(request):

    latest_question_list = Question.objects.order_by("-published_at")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question with id %s does not exist"%question_id)

    # continue as now question will be defined
    context = {"question": question}
    return render(request, 'polls/detail.html', context)
    # return HttpResponse("You're looking at question %s." % question.id)


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question with id %s does not exist"%question_id)

    return render(request, 'polls/results.html', {"question":question})


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST.get("choice"))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {"question": question, "error message": "you didnt select a choice"})

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('results', args={question.id,}))