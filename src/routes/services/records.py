import routes.models as models
import routes.services.conf as conf
import routes.services.utils as utils
from django.db.models import F



class record:
    def get_for_route(self,route_id,max_return=20):
        query = models.RouteRecord.objects.select_related('user__user__profile').filter(route=route_id)[:max_return]
        data = list(query.annotate(username=F('user__user__username')).values('username','date','record_type'))

        data = self.update_data_with_record_type_name(data)
        return data

    def update_data_with_record_type_name(self,data):
        for item in data:
            item.update( {"record_type_name":conf.ClimbStatus(item['record_type']).name})
        return data
        
# def _get_record_type_name(query):
#     record_type_name = [conf.ClimbStatus(rr.record_type).name for rr in query]
#     return record_type_name

# def _get_record_data(query):
#     username = []
#     record_type_name = []
#     for rr in query:
#         username.append(_get_username(rr))
#         record_type_name.append(_get_record_type(rr))

#     record_type_name = [conf.ClimbStatus(rr.record_type).name for rr in query]
#     return record_type_name

# def _get_username(rr):
#     return rr.user.user.username

def _get_record_type(rr):
    return conf.ClimbStatus(rr.record_type).name

# query.values_list('user','record_type')