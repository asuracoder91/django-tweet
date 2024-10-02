from django.shortcuts import render
from .models import Tweet


# Create your views here.
def tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "tweets.html",
        {
            "tweets": tweets,
            "title": "Tweets",
        },
    )
