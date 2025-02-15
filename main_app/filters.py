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
        fields = ['category'] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.queryset = self.queryset.filter(user=user)