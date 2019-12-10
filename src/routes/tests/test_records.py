from .base import RoutesTestCase
from django.test import TestCase
import routes.services.records as rec
import routes.tests.sampledata  as sampledata

class TestRecords(TestCase):
    def test_get_all_for_route(self):
        route_id = 1

        sampledata.create_auth_user()
        sampledata.route_set_active()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=2)

        r = rec.record()
        data = r.get_for_route(route_id)
        self.assertEqual(data[0]['username'],'Chevy Chase')
        self.assertEqual(data[0]['record_type'],1)
        self.assertEqual(data[0]['record_type_name'],'climbed')
        self.assertEqual(data[1]['record_type'],2)

