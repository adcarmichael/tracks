from .base import RoutesTestCase
from django.test import TestCase
import routes.services.records as rec
import routes.tests.sampledata as sampledata
import routes.models as models


class TestRecords(RoutesTestCase):
    def test_get_all_for_route(self):
        route_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=2)

        r = rec.record()
        data = r.get_for_route(route_id)
        self.assertEqual(data[0]['username'], 'Chevy Chase')
        self.assertEqual(data[0]['record_type'], 1)
        self.assertEqual(data[0]['record_type_name'], 'climbed')
        self.assertEqual(data[1]['record_type'], 2)


class TestRecordsDelete(RoutesTestCase):
    def test_delete_last_route_record_entry_for_user(self):
        user_id = 1
        route_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active()
        sampledata.gym_and_route_set()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=2)

        query_pre_list = list(models.RouteRecord.objects.all())

        rec.delete_last_route_record_entry_for_user(user_id, route_id)

        query = models.RouteRecord.objects.all()

        self.assertEqual(query.count(), 1)
        self.assertEqual(len(query_pre_list), 2)

    def test_delete_all_for_user(self):
        user_id = 1
        route_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active()
        sampledata.gym_and_route_set()
        sampledata.create_sample_route_record()
        sampledata.create_sample_route_record(record_type=2)

        query_pre_list = list(models.RouteRecord.objects.all())

        rec.delete_route_record_for_user(user_id, route_id)

        query = models.RouteRecord.objects.all()

        self.assertEqual(query.count(), 0)
        self.assertEqual(len(query_pre_list), 2)


class TestUserRecord(RoutesTestCase):
    def test_get_for_user(self):

        user_id = 1
        route_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active(
            colour='purple')
        sampledata.create_sample_route_record(route_id=route_id)

        record = rec.record()
        data = record.get_for_user(user_id)

        self.assertEqual(data[0]['grade'], 1)
        self.assertEqual(data[0]['grade_sub'], 4)
        self.assertEqual(data[0]['record_type_name'], 'climbed')

    def test_get_for_user_w_no_record(self):

        user_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active(
            colour='purple')

        record = rec.record()
        data = record.get_for_user(user_id)
        self.assertEqual(data, [])

    def test_get_for_user_w_max_return(self):

        user_id = 1
        route_id = 1

        sampledata.create_auth_user()
        sampledata.add_gym()
        sampledata.route_set_active(
            colour='purple')

        record = rec.record(max_return=2)
        sampledata.create_sample_route_record(route_id=route_id)
        sampledata.create_sample_route_record(route_id=route_id)
        sampledata.create_sample_route_record(route_id=route_id)

        data = record.get_for_user(user_id)
        self.assertEqual(len(data), 2)
