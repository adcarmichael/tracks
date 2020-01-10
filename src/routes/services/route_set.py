from datetime import datetime
from routes.models import Route, RouteRecord, RouteSet, Gym
from routes.services import route_set as RS


def _filter_to_only_active(query):
    date_now = datetime.now().date()
    return query.filter(up_date__lt=date_now, down_date__gt=date_now)


def _filter_to_only_inactive(query):
    date_now = datetime.now().date()
    return query.filter(down_date__lt=date_now)


def get_route_set_id_for_grade_active(gym_id, grade):
    query = RouteSet.objects.filter(gym=gym_id, routes__grade=grade)
    query = _filter_to_only_active(query)

    if query:
        id = query[0].id
    else:
        id = []
    return id


def get_route_set_id_for_grade_inactive(gym_id, grade, ind=0):
    query = RouteSet.objects.filter(gym=gym_id, routes__grade=grade)
    query = _filter_to_only_inactive(query)

    if query:
        id = query[ind].id
    else:
        id = []
    return id


def create_route_set(gym_id, grade, grade_sub, up_date, down_date=None, zone='', number=[]):

    if not number:
        number = range(1, len(grade_sub)+1)

    is_gym = Gym.objects.filter(id=gym_id).exists()

    if is_gym:

        gym = Gym.objects.get(id=gym_id)

        rs = RouteSet.objects.create(up_date=up_date, gym=gym, zone=zone)

        if down_date:
            rs.down_date = down_date
            rs.save()

        is_multi_grade = isinstance(grade, list)

        for ind, ind_grade_sub in enumerate(grade_sub):

            if is_multi_grade:
                grade_tmp = grade[ind]
            else:
                grade_tmp = grade

            Route.objects.create(grade=grade_tmp,
                                 grade_sub=ind_grade_sub,
                                 number=number[ind],
                                 route_set=rs)
