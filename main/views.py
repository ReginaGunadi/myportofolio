from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Regina Gunadi",
        "npm": "2506542852",
        "study_program": "S1 Ilmu Komputer",
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