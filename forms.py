from django import forms

from leads.models import TalkWithUs
from leads.models import BookBuilding
from leads.models import VisitBuilding
from leads.models import Register


class TalkWithUsForm(forms.ModelForm):
    class Meta:
        model = TalkWithUs

class BookBuildingForm(forms.ModelForm):
    class Meta:
        model = BookBuilding

class VisitBuildingForm(forms.ModelForm):
    class Meta:
        model = VisitBuilding

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
