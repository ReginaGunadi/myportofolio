from django.urls import path

from main.views import show_main, show_experience, show_award, create_experience, delete_experience, get_experience_json, create_award, get_award_json, delete_award
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("award/", show_award, name="show_award"),

    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),

    path("award/add/", create_award, name="create_award"),
    path("award/<uuid:award_id>/delete/",delete_award,name="delete_award"),
    path("api/award/", get_award_json, name="get_award_json"),

]