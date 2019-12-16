from django.test import TestCase
import tracks
from django.db import connection


class RoutesTestCase(TestCase):
    def setUp(self):
        clear_postgres_pk()

def clear_postgres_pk():
    # The below code only works for postgres
    current_engine = get_current_db_engine()
    is_postgres = "django.db.backends.postgresql" == current_engine
    if is_postgres:
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE routes_gym RESTART IDENTITY CASCADE;')
            cursor.execute(
                'TRUNCATE routes_routerecord RESTART IDENTITY CASCADE;')
            cursor.execute('TRUNCATE routes_profile RESTART IDENTITY CASCADE;')
            cursor.execute('TRUNCATE auth_user RESTART IDENTITY CASCADE;')
            cursor.execute('TRUNCATE routes_route RESTART IDENTITY CASCADE;')

def get_current_db_engine():
    return tracks.settings.DATABASES['default']['ENGINE']