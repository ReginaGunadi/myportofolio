import django_filters
from main.models import Award

class AwardFilter(django_filters.FilterSet):
    class Meta: 
        model = Award
        fields = {
            "category" : ["exact"],
        }