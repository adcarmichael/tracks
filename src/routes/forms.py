from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from routes.services.conf import GradeSub, Grade
from routes.services import security
from routes.models import Zone
import logging

logger = logging.getLogger(__name__)


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
            ind_1 = ind+1
            field_name = f'grade_sub_{ind_1}'
            self.fields[field_name] = forms.ChoiceField(
                choices=CHOICES_grade_sub, label=f'Route #{ind_1}', widget=forms.widgets.Select(attrs={'class': 'uk-select'}))


class RouteSetCreateForm():
    fields_prefix = {'route_num': 'route_num_',
                     'grade': 'grade_', 'grade_sub': 'grade_sub_'}
    route_num_max = 300

    def __init__(self, gym_id, request=[]):
        self.set_gym_id(gym_id)
        self.context = []
        self.cleaned = {}
        self.set_choices(gym_id)
        self.valid = True
        if request:
            self.post_request(gym_id, request)
        else:
            self.get_request(gym_id)

    def is_valid(self):
        return self.valid

    def set_choices(self, gym_id):
        self.grade_sub_choices = [e.name for e in GradeSub]
        self.grade_choices = [e.name for e in Grade]
        self.zone_choices = self.get_zone_choices()

    def get_context(self):
        return self.context

    def get_request(self, gym_id):
        self.context = self.get_init_context()
        self.context['message'] = self.message

    def post_request(self, gym_id, request):
        self.context = self.get_init_context()
        num_rows = self.get_num_rows(request)
        route_number = []
        grade = []
        grade_sub = []
        for row in range(1, num_rows+1):
            route_number.append(
                int(request.POST[self.fields_prefix['route_num'] + str(row)]))
            grade.append(request.POST[self.fields_prefix['grade'] + str(row)])
            grade_sub.append(
                request.POST[self.fields_prefix['grade_sub'] + str(row)])

        zone = request.POST['zone']
        up_date = request.POST['up_date']
        down_date = request.POST['down_date']

        self.check_date_str_is_clean(up_date, name='up_date')
        self.check_date_str_is_clean(down_date, name='down_date')
        self.check_choices_generic_is_clean('grade', grade, self.grade_choices)
        self.check_choices_generic_is_clean(
            'grade_sub', grade_sub, self.grade_sub_choices)
        self.check_choices_generic_is_clean('zone', [zone], self.zone_choices)
        self.check_route_num_is_clean(route_number)

        self.context['route_data'] = zip(route_number, grade, grade_sub)
        self.context['message'] = self.message

    def set_gym_id(self, gym_id):
        self.gym_id = gym_id
        valid = security.Validate().gym(gym_id)
        if not valid:
            self.valid = valid
            self.message.append('Gym does not exist')

    def get_zone_choices(self):

        query = Zone.objects.filter(gym=self.gym_id)
        if query:
            zones = [a.name for a in query]
            return zones
        else:
            return ['None']

    def check_date_str_is_clean(self, date_str, name='Date'):
        if type(date_str) is not str:
            self.valid = False
            msg = f'{name} is not a string.'
            self.message.append(msg)
            logger.warning(msg)
        if '-' not in date_str:
            self.valid = False
            msg = f'{name} is not a valid format'
            self.message.append(msg)
            logger.warning(msg)
        self.cleaned[name] = date_str

    def check_route_num_is_clean(self, route_num):
        if route_num:
            for ind, rn in enumerate(route_num):
                if type(rn) is not int:
                    msg = f'Route {ind} is not integer'
                    self.message.append(msg)
                    logger.warning(msg)
                    self.valid = False
                if rn > self.route_num_max or rn < 1:
                    msg = f'Route {ind} equals {rn} which is invalid'
                    self.message.append(msg)
                    logger.warning(msg)
                    self.valid = False
        else:
            self.message.append(f'No route numbers were recieved')
            self.valid = False
        self.cleaned['number'] = route_num

    def check_choices_generic_is_clean(self, name, grade_gen, choices):
        if grade_gen:
            for ind, rn in enumerate(grade_gen):
                if type(rn) is not str:
                    msg = f'{ind} is not String'
                    self.message.append(msg)
                    logger.warning(msg)
                    self.valid = False
                if rn not in choices:

                    msg = f'{name} {ind} equals {rn} which is invalid'
                    self.message.append(msg)
                    logger.warning(msg)
                    self.valid = False
        else:
            msg = f'No {name} were recieved'
            self.message.append(msg)
            logger.warning(msg)
            self.valid = False

        self.cleaned[name] = grade_gen

    def get_num_routes_from_request(request):
        keys = [key for key in request.POST.keys()]

    def get_num_rows(self, request):
        num_rows = 0
        for key, value in request.POST.items():
            if self.fields_prefix['route_num'] in key:
                num_rows += 1
        return num_rows

    def get_init_route_data(self):
        route_number = [1]
        grade = [self.grade_choices[3]]
        grade_sub = [self.grade_sub_choices[3]]
        route_data = zip(route_number, grade, grade_sub)
        return route_data

    def get_init_context(self):
        self.message = []

        init_context = {'grade_choices': self.grade_choices,
                        'grade_sub_choices': self.grade_sub_choices,
                        'zone_choices': self.zone_choices,
                        'route_data': self.get_init_route_data()}
        return init_context
