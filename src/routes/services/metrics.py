from django.db.models import Count
from django.db.models import Q
from routes.models import RouteRecord
import routes.services.conf as conf
from routes.models import RouteSet,Route
from routes.services import route_set as RS


# def get_most_recorded_grade(gym_id=[],user_id=[])
#     if 
#     fieldname = 'myCharField'
#     MyModel.objects.values(fieldname)
#         .order_by(fieldname)
#         .annotate(the_count=Count(fieldname))

cs = conf.ClimbStatus.climbed.value
os = conf.ClimbStatus.onsight.value

def get_total_climbs_for_route(route_id):
    if not isinstance(route_id, (list,)):
            route_id = [route_id]
    

    n_climbs = [0]*len(route_id)
    for ind, r_id in enumerate(route_id):
        n_climbs[ind] = RouteRecord.objects.filter( Q(route=r_id) & (Q(record_type=os) | Q(record_type=cs))).count()
        
    return n_climbs


def get_percentage_complete_for_active_grade(gym_id,user_id,grade):
    route_set_id = RS.get_route_set_id_for_grade_active(gym_id,grade)
    perc_complete = get_route_set_perc_complete(route_set_id,user_id)
    return perc_complete

def get_percentage_complete_for_previously_active_grade(gym_id,user_id,grade):
    route_set_id = RS.get_route_set_id_for_grade_inactive(gym_id,grade)
    perc_complete = get_route_set_perc_complete(route_set_id,user_id)
    return perc_complete

def get_route_set_perc_complete(route_set_id,user_id):
    query = Route.objects.filter(route_set=route_set_id)
    num_routes = query.count()
    query = query.filter(Q(routerecord__user=user_id) & (Q(routerecord__record_type=os) | Q(routerecord__record_type=cs))).distinct('id')
    num_climbed = query.count()

    if num_routes > 0:
        percentage = num_climbed/num_routes*100
    else:
        percentage = 0
    return percentage