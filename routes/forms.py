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

    grade_sub_1 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #1', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_2 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #2', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_3 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #3', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_4 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #4', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_5 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #5', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_6 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #6', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_7 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #7', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_8 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #8', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_9 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #9', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_10 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #10', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_11 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #11', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_12 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #12', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_13 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #13', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_14 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #14', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_15 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #15', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_16 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #16', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_17 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #17', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_18 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #18', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_19 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #19', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_20 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #20', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_21 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #21', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_22 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #22', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_23 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #23', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
    grade_sub_24 = forms.ChoiceField(
        choices=CHOICES_grade_sub, label='Route #24', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))
