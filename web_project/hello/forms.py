from django import forms
from hello.models import Person

class PersonEdidForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name","lastname","birthdate")