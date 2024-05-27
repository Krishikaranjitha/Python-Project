from django.forms import ModelForm
from .models import *
class Studentform_Form(ModelForm):
    class Meta:
        model=Studentform
        fields='__all__'