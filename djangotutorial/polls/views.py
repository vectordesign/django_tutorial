from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import render

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
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)