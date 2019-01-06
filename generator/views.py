from django.shortcuts import render, redirect
from run import DiscoveryGenerator
from generator.models import Response
import datetime as dt

from .forms import DailyForm

# Create your views here.
def homepage(request):
    prompts = DiscoveryGenerator()
    prompt = prompts.choose()

    today_date = dt.datetime.now().date()
    today_date_lg = dt.datetime.strftime(today_date, '%B %d, %Y')
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')

    # if request.method == 'POST':
    #     Response.objects.create(response_text=request.POST['response_text'],
    #     response_prompt=request.POST['prompt_text'],
    #     date=today_date_st
    #     )
    #
    # responses = Response.objects.all()

    if request.method == 'POST':
        form = DailyForm(request.POST)
        Response.objects.create(prompt=request.POST[form.prompt],
            response=request.POST[form.response],
            date=today_date_st
            )
    else:
        form = DailyForm()

    return render(request, 'home.html', {'form': form})

def review(request):

    today_date = dt.datetime.now().date()
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')

    form = DailyForm(request.POST)
    Response.objects.create(prompt=request.POST['prompt'],
        response=request.POST['response'],
        date=today_date_st
        )
    responses = Response.objects.all()
    return render(request, 'review.html',
                    {'responses':
                        responses,
                    }
                )
