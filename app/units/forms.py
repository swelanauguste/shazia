from django import forms

from .models import Unit


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"
        widgets = {
            "remarks": forms.Textarea(attrs={"rows": 2}),
        }
