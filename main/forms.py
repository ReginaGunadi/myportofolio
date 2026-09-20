from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience, Award

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at"
        ]

        labels = {
            "title": "Experience title",
            "description": "Experience description",
            "category": "Experience category",
            "thumbnail" : "Experience photo",
            "started_at": "Experience start date",
            "ended_at": "Experience end date"
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Add your experience title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Internship, research, volunteer, part-time, full-time, freelance",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://www.google.com/",
                }
            ),
            "started_at": TextInput(
                attrs={
                    "placeholder": "2026-09-01",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "2026-09-02",
                }
            ),
        }


class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "description",
            "category",
            "image",
        ]

        labels = {
            "title": "Award title",
            "description": "Award description",
            "category": "Award category",
            "image" : "Award photo",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Add your award title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your award",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Math, music, tech, other",
                }
            ),
            "image": URLInput(
                attrs={
                    "placeholder": "https://www.google.com/",
                }
            ),
        }