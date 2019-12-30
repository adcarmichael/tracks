from datetime import datetime
from routes.models import Route, RouteRecord, RouteSet
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
