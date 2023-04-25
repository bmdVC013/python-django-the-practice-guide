from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    MONTH_MAPPER = {
        "january": "Eat no meat for the entire month!",
        "february": "Walk for at least 20 minutes every day!",
        "march": "Learn Django for at least 20 minutes every day!"
    }

    return HttpResponse(MONTH_MAPPER[month]) if MONTH_MAPPER.get(month) else HttpResponseNotFound("This month is not supported!")
