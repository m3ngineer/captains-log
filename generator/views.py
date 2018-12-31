from django.shortcuts import render, redirect
from run import DiscoveryGenerator
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

    return render(request, 'home.html',
                {'prompt':
                    prompt,
                'today_str':
                    today_str
                }
            )
