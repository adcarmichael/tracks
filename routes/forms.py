from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from routes.services.conf import GradeSub, Grade


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class AddRouteSetForm_Eden(forms.Form):
    # grade = forms.CharField(label='grade', max_length=100)
    # grade_sub = forms.CharField(label='grade', max_length=100)

    # ((tag.name,tag.value) for tag in GradeSub)

    CHOICES_grade_sub = [(e.value, e.name) for e in GradeSub]
    CHOICES_grade = [(e.value, e.name) for e in Grade]
    grade = forms.ChoiceField(choices=CHOICES_grade, widget=forms.widgets.Select(
        attrs={'class': 'uk-select', 'uk-tooltip': 'Specify the Colour of the new route set.'}),  label='Colour')
    up_Date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'uk-input', 'uk-tooltip': 'The date that the route set will go live. Click on the date picker at the far right.'}), label='Up Date')
    down_Date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'uk-tooltip': 'The date that the route set will be taken down. Click on the date picker at the far right.', 'type': 'date', 'class': 'uk-input'}), label='Down Date')

    grade_sub = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #1', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
