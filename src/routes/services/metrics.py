from django.db.models import Count
from django.db.models import Q
from routes.models import RouteRecord
import routes.services.conf as conf

# def get_most_recorded_grade(gym_id=[],user_id=[])
#     if 
#     fieldname = 'myCharField'
#     MyModel.objects.values(fieldname)
#         .order_by(fieldname)
#         .annotate(the_count=Count(fieldname))

def get_total_climbs_for_route(route_id):
    if not isinstance(route_id, (list,)):
            route_id = [route_id]
    cs = conf.ClimbStatus.climbed.value
    os = conf.ClimbStatus.onsight.value

    n_climbs = [0]*len(route_id)
    for ind, r_id in enumerate(route_id):
        n_climbs[ind] = RouteRecord.objects.filter( Q(route=r_id) & (Q(record_type=os) | Q(record_type=cs))).count()
        
    return n_climbs


