import routes.models as models
import services.conf as conf
import services.utils as utils



class record:
    def get_all_for_route(self,route_id,max_return=20):
        query = models.RouteRecord.objects.filter(id=route_id)[:max_return].values

        record_type_name = _get_record_type_name(query)

        data = ['number':rr.number,'record_type':record_tyoe_name]

def _get_record_type_name(query):
    record_type_name = [conf.ClimbStatus(rr.record_type).name for rr in query]
    return record_type_name