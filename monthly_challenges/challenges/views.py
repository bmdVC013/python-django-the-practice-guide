from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    MONTH_CHALLENGE_MAPPER = {
        "january": "Eat no meat for the entire month!",
        "february": "Walk for at least 20 minutes every day!",
        "march": "Learn Django for at least 20 minutes every day!",
    }

    return HttpResponseNotFound("This month is not supported!") if MONTH_CHALLENGE_MAPPER.get(month) == None else HttpResponse(MONTH_CHALLENGE_MAPPER[month])
