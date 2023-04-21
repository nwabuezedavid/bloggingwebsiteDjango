from django.forms import ModelForm
from . models import *


class detailMoldelForm(ModelForm):
    class Meta:
        model = blogDetail
        fields = "__all__"

