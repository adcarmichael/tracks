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

    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )
    CHOICES_grade_sub = [(e.value, e.name) for e in GradeSub]
    CHOICES_grade = [(e.value, e.name) for e in Grade]
    Colour = forms.ChoiceField(choices=CHOICES_grade)
    amount = forms.DecimalField()
    Up_Date = forms.DateField()
    Down_Date = forms.DateField()

    SubGrade = forms.ChoiceField(choices=CHOICES_grade_sub)
