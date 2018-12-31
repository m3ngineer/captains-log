from django.shortcuts import render, redirect
from run import DiscoveryGenerator
from generator.models import Response
import datetime as dt


# Create your views here.
def homepage(request):
    prompts = DiscoveryGenerator()
    prompt = prompts.choose()

    today = dt.datetime.now().date()
    today_str = '{} {}, {}'.format(today.strftime("%B"),
        today.strftime("%d"),
        today.strftime("%Y")
        )

    today_num = today

    if request.method == 'POST':
        Response.objects.create(response=request.POST['response_text'],
        date=today_num,
        prompt=prompt
        # response_id=Response.id
        )

    responses = Response.objects.all()

    return render(request, 'home.html',
                {'prompt':
                    prompt,
                'today_str':
                    today_str,
                'responses':
                    responses
                }
            )
