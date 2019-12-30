from datetime import datetime




def _filter_to_only_active_routes(query):
    date_now = datetime.now().date()
    return query.filter(route_set__up_date__lt=date_now,route_set__down_date__gt=date_now)