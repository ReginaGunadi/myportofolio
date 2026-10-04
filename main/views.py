import datetime

from django.shortcuts import render

from main.models import Experience, Award
from main.forms import ExperienceForm, AwardForm

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required, permission_required 

from django.views.decorators.http import require_POST


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')

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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your account has been made. Continue login.")
        return redirect("main:login")

    context = {
        "name": "Regina Gunadi",
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
        "name": "Regina Gunadi",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# Experience Section
def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Regina Gunadi",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        context = {
            "name": "Regina Gunadi",
        }
        return render(request, "forbidden.html", context, status=403)
    
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
        context = {
            "name": "Regina Gunadi",
        }
        return render(request, "forbidden.html", context, status=403)
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience has successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@permission_required("main.change_experience", raise_exception=True)
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

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for exp in experience:
        starred_users = exp.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.ambil_isi_list,
                "category": exp.category,
                "thumbnail" : exp.thumbnail,
                "started_at": exp.started_at,
                "ended_at": exp.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    
    return JsonResponse(data, safe=False)




# Award Section
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
def create_award(request):
    if not request.user.is_superuser:
        context = {
            "name": "Regina Gunadi",
        }
        return render(request, "forbidden.html", context, status=403)
    
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
    if not request.user.is_superuser:
        context = {
            "name": "Regina Gunadi",
        }
        return render(request, "forbidden.html", context, status=403)

    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Award has successfully deleted!")
        return redirect("main:show_award")

    return redirect("main:show_award")

@permission_required("main.change_award", raise_exception=True)
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


# Toggle Star
@login_required(login_url="/login/")
def toggle_star(request, item_type, item_id):
    if request.method == "POST":
        if item_type == 'experience':
            obj = get_object_or_404(Experience, pk=item_id)
            redirect_url = "main:show_experience"
        elif item_type == 'award':
            obj = get_object_or_404(Award, pk=item_id)
            redirect_url = "main:show_award"
        else:
            return redirect("main:show_main")


        if request.user in obj.starred_by.all():
            obj.starred_by.remove(request.user)
        else:
            obj.starred_by.add(request.user)
            
        return redirect(redirect_url)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)