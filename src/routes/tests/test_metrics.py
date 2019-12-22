from django.db.models import Count
from .base import RoutesTestCase
from django.test import TestCase
import routes.services.records as rec
import routes.tests.sampledata  as sampledata
from routes.models import Route,RouteRecord,RouteSet
from routes.services import metrics
import routes.services.conf as conf
from routes.services import route_set as RS
from routes.services import routes as R
from django.db.models import Q

class TestMetrics(RoutesTestCase):
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
        sampledata.add_gym()
        sampledata.route_set_active()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(record_type=conf.ClimbStatus.attempted.value)
        route_id = 1
        n_climbs = metrics.get_total_climbs_for_route(route_id)
        self.assertEqual(n_climbs[0],3)

class TestPercComplete(RoutesTestCase):

    def test_get_perc(self):
        cs = conf.ClimbStatus.climbed.value
        os = conf.ClimbStatus.onsight.value

        sampledata.create_auth_user() # user_id = 1
        sampledata.create_auth_user(name='me') 
        sampledata.add_gym()
        sampledata.route_set_active(colour='blue')# route_set_id=2
        sampledata.route_set_inactive() # route_set_id=2

        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=2, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(user_id=2,route_id=2, record_type=conf.ClimbStatus.climbed.value)
        
        gym_id = 1
        user_id = 1
        grade = 5

        perc_complete = metrics.get_percentage_complete_for_active_grade(gym_id,user_id,grade)
        self.assertEqual(perc_complete,50)

    def test_get_perc_second_user(self):
        cs = conf.ClimbStatus.climbed.value
        os = conf.ClimbStatus.onsight.value

        sampledata.create_auth_user() # user_id = 1
        sampledata.create_auth_user(name='me') 
        sampledata.add_gym()
        sampledata.route_set_active(colour='blue')# route_set_id=2
        sampledata.route_set_inactive() # route_set_id=2

        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=2, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(user_id=2,route_id=2, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(user_id=2,route_id=1, record_type=conf.ClimbStatus.climbed.value)

        gym_id = 1
        user_id = 2
        grade = 5

        perc_complete = metrics.get_percentage_complete_for_active_grade(gym_id,user_id,grade)
        self.assertEqual(perc_complete,100)

    def test_get_perc_prev_active(self):
        cs = conf.ClimbStatus.climbed.value
        os = conf.ClimbStatus.onsight.value

        sampledata.create_auth_user() # user_id = 1
        sampledata.create_auth_user(name='me') 
        sampledata.add_gym()
        sampledata.route_set_active(colour='blue')# route_set_id=2
        sampledata.route_set_inactive() # route_set_id=2

        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(route_id=1, record_type=conf.ClimbStatus.onsight.value)
        sampledata.create_sample_route_record(route_id=2, record_type=conf.ClimbStatus.attempted.value)
        sampledata.create_sample_route_record(user_id=2,route_id=2, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(user_id=2,route_id=1, record_type=conf.ClimbStatus.climbed.value)

        sampledata.create_sample_route_record(user_id=2,route_id=3, record_type=conf.ClimbStatus.climbed.value)
        sampledata.create_sample_route_record(user_id=2,route_id=4, record_type=conf.ClimbStatus.attempted.value)

        gym_id = 1
        user_id = 2
        grade = 7
        perc_complete = metrics.get_percentage_complete_for_previously_active_grade(gym_id,user_id,grade)
        self.assertEqual(perc_complete,50)
