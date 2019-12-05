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


class GymCreateForm(forms.Form):
    Name = forms.CharField(max_length=300, help_text='Name of Climbing Gym')
    City = forms.CharField(max_length=300, help_text='City of Climbing Gym')
    Email = forms.EmailField(help_text='Email of Climbing Gym')


class RouteSetForm(forms.Form):
    up_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'uk-input', 'uk-tooltip': 'The date that the route set will go live. Click on the date picker at the far right.'}), label='Up Date')
    down_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'uk-tooltip': 'The date that the route set will be taken down. Click on the date picker at the far right.', 'type': 'date', 'class': 'uk-input'}), label='Down Date')


class AddRouteSetForm_Eden(forms.Form):
    # grade = forms.CharField(label='grade', max_length=100)
    # grade_sub = forms.CharField(label='grade', max_length=100)

    # ((tag.name,tag.value) for tag in GradeSub)

    CHOICES_grade_sub = [(e.value, e.name) for e in GradeSub]
    CHOICES_grade = [(e.value, e.name) for e in Grade]

    grade = forms.ChoiceField(choices=CHOICES_grade, widget=forms.widgets.Select(
        attrs={'class': 'uk-select', 'uk-tooltip': 'Specify the Colour of the new route set.'}),  label='Colour')
    up_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'uk-input', 'uk-tooltip': 'The date that the route set will go live. Click on the date picker at the far right.'}), label='Up Date')
    down_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'uk-tooltip': 'The date that the route set will be taken down. Click on the date picker at the far right.', 'type': 'date', 'class': 'uk-input'}), label='Down Date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        num_routes = 41
        CHOICES_grade_sub = [(e.value, e.name) for e in GradeSub]
        for ind in range(num_routes):
            field_name = f'grade_sub_{ind}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES_grade_sub, label=f'Route #{ind}', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
