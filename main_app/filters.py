# filters.py
import django_filters
from .models import HiddenGem

class HiddenGemFilter(django_filters.FilterSet):
    class Meta:
        model = HiddenGem
        fields = ['category', "user"] 

class UserHiddenGemFilter(django_filters.FilterSet):
    class Meta:
        model = HiddenGem
        fields = ['category', "title"] 