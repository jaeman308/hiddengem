# filters.py
import django_filters
from .models import HiddenGem

class HiddenGemFilter(django_filters.FilterSet):
    class Meta:
        model = HiddenGem
        fields = ["title",'category', "user"] 