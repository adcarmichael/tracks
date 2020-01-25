import routes.models as models
import routes.services.conf as conf
import routes.services.utils as utils
from django.db.models import F


class record:
    def __init__(self, max_return=20, is_reversed=False):
        self.max_return = max_return
        self.is_reversed = is_reversed

    def get_for_route(self, route_id):
        query = models.RouteRecord.objects.select_related('user__user__profile',
                                                          'route', 'route__route_set__gym').filter(route=route_id)

        data = self._get_data(query)

        return data

    def update_data_with_record_type_name(self, data):
        for item in data:
            item.update(
                {"record_type_name": conf.ClimbStatus(item['record_type']).name})
        return data

    def _get_data(self, query):

        if self.is_reversed:
            query = query.order_by('-id')

        query = query[:self.max_return]

        data = list(query.annotate(gym_id=F('route__route_set__gym'), number=F('route__number'), grade=F('route__grade'), username=F('user__user__username'), grade_sub=F(
            'route__grade_sub')).values('username', 'grade', 'grade_sub', 'date', 'record_type', 'route', 'number', 'gym_id'))
        data = self.update_data_with_record_type_name(data)

        return data

    def get_for_user(self, user_id):

        query = models.RouteRecord.objects.select_related('user__user__profile',
                                                          'route').filter(user=user_id)
        data = self._get_data(query)
        return data


class user_record:
    def __init__(self, user_id, gym_id=[]):
        self.user_id = user_id


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


def delete_route_record_for_user(user_id, route_id):
    query = models.RouteRecord.objects.filter(
        user=user_id).filter(route=route_id)
    if query:
        query.delete()


def delete_last_route_record_entry_for_user(user_id, route_id):
    query = models.RouteRecord.objects.filter(user=user_id).filter(
        route=route_id).order_by('-id').first()
    if query:
        query.delete()


def _get_record_type(rr):
    return conf.ClimbStatus(rr.record_type).name

# query.values_list('user','record_type')
