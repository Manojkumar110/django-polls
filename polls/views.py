from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

# def index(request):
    # q = Question.objects.all()
    # print(q)
    # q = Question.objects.create(question_text = "What's new ?", pub_date=timezone.now())
    # q.save()
    # q = Question.objects.filter(id=2)
    # print(q)
    # q = Question.objects.filter(question_text__startswith = 'What')
    # print(q)
    # current_year = timezone.now().year
    # q = Question.objects.filter(pub_date__year = current_year)
    # print(q)
    # q = Question.objects.get(id=2)
    # print(q)
    # q = Question.objects.get(pk=2)
    # print(q.was_published_recently())
    # --------------Choice Model------------------------
    # print(q.choice_set.all())
    # q.choice_set.create(choice_text="Not much", votes=0)
    # q.choice_set.create(choice_text="The sky", votes=0)
    # c = q.choice_set.create(choice_text="Just hacking again", votes=0)  
    # print(c.question)
    # print(q.choice_set.count())
    # print(Choice.objects.filter(question__pub_date__year=current_year))
    # print(q.choice_set.filter(choice_text__startswith="Just hacking"))
    # q.delete()
    # return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     print('latest_question_list :', latest_question_list)
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     print('latest_question_list_str :', output)
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(' Question Does Not exist')
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question, 
            "error_message": "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
   

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})





# class base view :-


# from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, "polls/detail.html", {
#             "question": question, 
#             "error_message": "You didn't select a choice.",})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"
