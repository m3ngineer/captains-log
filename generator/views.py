from django.shortcuts import render, redirect
from run import DiscoveryGenerator
from generator.models import Response
import datetime as dt


# Create your views here.
def homepage(request):
    prompts = DiscoveryGenerator()
    prompt = prompts.choose()

    today_date = dt.datetime.now().date()
    today_date_lg = dt.datetime.strftime(today_date, '%B %d, %Y')
    today_date_st = dt.datetime.strftime(today_date, '%y-%m-%d')

    if request.method == 'POST':
        Response.objects.create(response=request.POST['response_text'],
        date=today_date_st,
        prompt=prompt
        )

    responses = Response.objects.all()

    return render(request, 'home.html',
                {'prompt':
                    prompt,
                'today_date_lg':
                    today_date_lg,
                'responses':
                    responses
                }
            )
