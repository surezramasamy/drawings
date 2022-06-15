
from django import forms
from .models import Drawings_2D


class drgform(forms.ModelForm):
    class Meta:
        model = Drawings_2D
        fields = ['Model_Name', 'Sub_Assembly_Name']

class drguploadform(forms.ModelForm):
    class Meta:
        model = Drawings_2D
        fields = ('Model_Name','Sub_Assembly_Name','Child_part','Drawing1','Drawing2','Photo1','Photo2','Process_Instructions')
