import datetime

from django.shortcuts import render

from main.models import Experience, Award
from main.forms import ExperienceForm, AwardForm

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied  


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')

    context = {
        "name": "Regina Gunadi",
        "npm": "2506542852",
        "study_program": "Bachelor of Computer Science",
        "bio": (
            "Undergraduate Computer Science student at Universitas Indonesia. "
            "Currently exploring data science and machine learning. "
            "A lifelong learner, pianist, math-tech lover and hater."
        ),
        "last_login": last_login,
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


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience has been added!")
        return redirect("main:show_experience")

    context = {
        "name": "Regina Gunadi",
        "form": form,
        "item_type": "experience",
        "action_type": "create", 
        "get_create_new_item_url": reverse("main:create_experience"),
        "get_show_all_item_url": reverse("main:show_experience"),
    }
    return render(request, "generic_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience has been edited!")
        return redirect("main:show_experience")

    context = {
        "name": "Regina Gunadi",
        "form": form,
        "item_type": "experience",
        "action_type": "edit",
        "get_create_new_item_url": reverse("main:create_experience"),
        "get_show_all_item_url": reverse("main:show_experience"),
    }

    return render(request, "generic_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    sort_by = request.GET.get("sort", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    if sort_by == "title_asc":
        experience = experience.order_by("title")
    if sort_by == "title_desc":
        experience = experience.order_by("-title")

    experience_json = serializers.serialize("json", experience, use_natural_foreign_keys=True)
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def create_award(request):
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New award has been added!")
        return redirect("main:show_award")

    context = {
        "name": "Regina Gunadi",
        "form": form,
        "item_type": "award",
        "action_type": "create",
        "get_create_new_item_url": reverse("main:create_award"),
        "get_show_all_item_url": reverse("main:show_award"),
    }
    return render(request, "generic_form.html", context)

@login_required(login_url="/login/")
def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Award has successfully deleted!")
        return redirect("main:show_award")

    return redirect("main:show_award")

@login_required(login_url="/login/")
def edit_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    
    form = AwardForm(request.POST or None, instance=award)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Award has been edited!")
        return redirect("main:show_award")

    context = {
        "name": "Regina Gunadi",
        "form": form,
        "item_type": "award",
        "action_type": "edit",
        "get_create_new_item_url": reverse("main:create_award"),
        "get_show_all_item_url": reverse("main:show_award"),
    }

    return render(request, "generic_form.html", context)

def get_award_json(request):
    title_query = request.GET.get("title", "").strip()
    sort_by = request.GET.get("sort", "").strip()
    award = Award.objects.all()

    if title_query:
        award = award.filter(title__icontains=title_query)

    if sort_by == "title_asc":
        award = award.order_by("title")
    if sort_by == "title_desc":
        award = award.order_by("-title")

    award_json = serializers.serialize("json", award, use_natural_foreign_keys=True)
    return HttpResponse(award_json, content_type="application/json")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Regina",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Regina",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_award(request, award_id):
    award = get_object_or_404(Experience, pk=award_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in award.starred_by.all():
            award.starred_by.remove(request.user)
        else:
            award.starred_by.add(request.user)

    return redirect("main:show_award")