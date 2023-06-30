from django.contrib.auth.forms import UserCreationForm
from app.models import User, Object
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )


class ObjectSearchForm(forms.Form):
    category = forms.ChoiceField(choices=Object.CategoryChoices.choices)
    city = forms.ChoiceField(choices=Object.CityChoices.choices)
    count = forms.IntegerField(min_value=1, max_value=100)
