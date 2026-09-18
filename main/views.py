from django.shortcuts import render

from main.models import Experience
from main.models import Award
from main.forms import ExperienceForm, AwardForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Regina Gunadi",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_award(request):
    json_response = get_award_json(request)
    
    award = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards = [awr.object for awr in award]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Regina Gunadi",
        "award_list": awards,
        "title_query": title_query,
    }

    return render(request, "award.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience has been added!")
        return redirect("main:show_experience")

    context = {
        "name": "Regina Gunadi",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")



def create_award(request):
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New award has been added!")
        return redirect("main:show_award")

    context = {
        "name": "Regina Gunadi",
        "form": form,
    }
    return render(request, "award_form.html", context)


def get_award_json(request):
    title_query = request.GET.get("title", "").strip()
    award = Award.objects.all()

    if title_query:
        award = award.filter(title__icontains=title_query)

    award_json = serializers.serialize("json", award)
    return HttpResponse(award_json, content_type="application/json")


def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Award has successfully deleted!")
        return redirect("main:show_award")

    return redirect("main:show_award")