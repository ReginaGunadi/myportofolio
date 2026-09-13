from django.shortcuts import render

from main.models import Experience
from main.models import Award
from main.filters import AwardFilter

def show_main(request):
    context = {
        "name": "Regina Gunadi",
        "npm": "2506542852",
        "study_program": "Bachelor of Computer Science",
        "bio": (
            "Undergraduate Computer Science student at Universitas Indonesia. "
            "Currently exploring data science and machine learning. "
            "A lifelong learner, pianist, math-tech lover and hater."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Regina Gunadi",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_award(request):
    awards = Award.objects.all() 
    awards_filter = AwardFilter(request.GET, queryset=awards)
    
    context = {
        "name": "Regina Gunadi",
        "filter": awards_filter,
    }

    return render(request, "award.html", context)