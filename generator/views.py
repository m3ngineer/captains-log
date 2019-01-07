from django.shortcuts import render, redirect
from run import DiscoveryGenerator
from generator.models import Response
import datetime as dt

from .forms import DailyForm

def homepage(request):
    prompts = DiscoveryGenerator()
    prompt = prompts.choose()

    today_date = dt.datetime.now().date()
    today_date_lg = dt.datetime.strftime(today_date, '%B %d, %Y')
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')
    responses = Response.objects.all()[::-1]

    form = DailyForm()
    form.fields['prompt'].widget.attrs['placeholder'] = 'Q: ' + prompt

    return render(request, 'home.html',
                    {'form':
                        form,
                    'responses':
                        responses,
                    'today_date_lg':
                        today_date_lg,
                    'prompt':
                        prompt
                    })

def review(request):

    today_date = dt.datetime.now().date()
    today_date_lg = dt.datetime.strftime(today_date, '%B %d, %Y')
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')

    form = DailyForm(request.POST)

    if request.method == 'POST':
        # Create a new response object in model
        Response.objects.create(prompt=request.POST['prompt'],
            response=request.POST['response'],
            date=today_date_st
            )

    # Collect responses
    responses = Response.objects.all()[::-1]

    return render(request, 'review.html',
                    {'responses':
                        responses,
                    'today_date_lg':
                        today_date_lg,
                    }
                )
def delete(request, response_id):

    today_date = dt.datetime.now().date()
    today_date_lg = dt.datetime.strftime(today_date, '%B %d, %Y')
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')

    Response.objects.get(id=response_id).delete()

    # Collect responses
    responses = Response.objects.all()[::-1]

    return render(request, 'review.html',
                    {'responses':
                        responses,
                    'today_date_lg':
                        today_date_lg,
                    }
                )
