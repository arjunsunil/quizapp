from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question,UserScore
from django.views.decorators.csrf import csrf_exempt
import datetime

@login_required(login_url="/login")
def home(request):
    questions = Question.objects.all
    return render(request, 'app/index.html', {'questions': questions})

def results(request):
    questions = Question.objects.all()
    score = 0
    for question in questions:
        answer = question.correct_ans
        entered_answer = request.POST.get(str(question.number))
        qs =Question.objects.filter(id=question.id)
        qs.update(entered_answer=entered_answer)
        if(entered_answer == answer):
            score+=1
    score*=10
    user=request.user
    date = datetime.datetime.now().strftime("%Y %b %d %a %I:%M %p")
    UserScore.objects.create(username=user,score=score,date=date)
    questions = Question.objects.all
    return render(request, 'app/results.html', {'score':score, 'questions':questions})

def other_results(request):
    results = UserScore.objects.all()
    return render(request, 'app/form.html', {'results': results})
