from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

MONTH_CHALLENGE_MAPPER = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "october": "Walk for at least 20 minutes every day!",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(MONTH_CHALLENGE_MAPPER.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(MONTH_CHALLENGE_MAPPER.keys())

    if month > 0 and month <= len(months):
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

    return HttpResponseNotFound("Invalid month!")


def monthly_challenge(request, month):
    try:

        challenge_text = MONTH_CHALLENGE_MAPPER[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()
