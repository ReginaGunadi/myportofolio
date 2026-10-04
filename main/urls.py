from django.urls import path

from main.views import show_main, show_experience, show_award
from main.views import create_experience, delete_experience, get_experience_json, edit_experience
from main.views import create_award, get_award_json, delete_award, edit_award
from main.views import register, login_user, logout_user
from main.views import toggle_star
from main.views import create_experience_ajax, create_award_ajax

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("award/", show_award, name="show_award"),

    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experience/<uuid:experience_id>/edit/",edit_experience,name="edit_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),

    path("award/add/", create_award, name="create_award"),
    path("award/<uuid:award_id>/delete/",delete_award,name="delete_award"),
    path("award/<uuid:award_id>/edit/",edit_award,name="edit_award"),
    path("api/award/", get_award_json, name="get_award_json"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path('star/<str:item_type>/<uuid:item_id>/', toggle_star, name='toggle_star'), 

    path("experiences/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("award/add-ajax/", create_award_ajax, name="create_award_ajax"),
]