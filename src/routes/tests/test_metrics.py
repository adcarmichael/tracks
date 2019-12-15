from django.db.models import Count
from .base import RoutesTestCase
from django.test import TestCase
import routes.services.records as rec
import routes.tests.sampledata  as sampledata
from routes.models import Route,RouteRecord
from routes.services import metrics
import routes.services.conf as conf

class TestMetrics(TestCase):
    # def test_get_most_recorded_grade(self):
    #     sampledata.create_auth_user()
    #     sampledata.route_set_active()
    #     sampledata.gym_and_route_set()
    #     sampledata.create_sample_route_record()
    #     fieldname = 'grade'
    #     breakpoint()
    #     query = Route.objects.filter(route_set__gym__id=1,routerecord__user=1).values(fieldname).order_by(fieldname).annotate(the_count=Count('routerecord__record_type'))

    #     for ind, r in enumerate(query):
    #         grade = r.grade
    #         if ind == 0:
    #             count_max = r.the_count
    def test_get_total_climbs_for_route(self):

        sampledata.create_auth_user()
        sampledata.route_set_active()
        sampledata.gym_and_route_set()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(record_type=conf.ClimbStatus.attempted.value)
        route_id = 1
        n_climbs = metrics.get_total_climbs_for_route(route_id)
        self.assertEqual(n_climbs[0],3)