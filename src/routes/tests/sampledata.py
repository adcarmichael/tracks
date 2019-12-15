import routes.services.dal as Dal
import routes.services.conf as conf
import os
from routes.models import RouteSet, Route, RouteRecord, Profile, Gym
from datetime import datetime, timedelta


dal = Dal.get_dal()

def route_set(gym_id, colour='black', grade=['high', 'medium'], down_date=None, up_date='03/06/2019'):
    dal.add_route_set(gym_id, colour, grade, up_date, down_date=down_date)

def gym_and_route_set(colour='black', grade=['high', 'medium'], down_date=None, up_date='03/06/2019', city='Edinburgh',  name='Eden Rocks Edinburgh', email='edinburgh@edenrockclimbing.com'):
    g = add_gym(city=city, name=name, email=email)
    route_set(g.id, colour=colour, grade=grade,
                         down_date=down_date, up_date=up_date)

def add_gym(city='Edinburgh', name='Eden Rocks Edinburgh', email='edinburgh@edenrockclimbing.com'):
    gym = dal.create_gym(name, email, city)
    return gym

def create_superuser_named_admin():
    os.system("""echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell""")

def create_auth_user(name='Chevy Chase', email='chevy@chase.com', password='chevyspassword'):
    from django.contrib.auth.models import User
    user = User.objects.create_user(
        name, email, password)

def route_set_active(colour='red'):
    now = datetime.now().date()
    td = timedelta(days=30)
    up_date_active = (now - td).strftime('%d/%m/%Y')
    down_date_active = (now + td).strftime('%d/%m/%Y')
    gym_and_route_set(colour=colour, up_date=up_date_active , down_date=down_date_active)
    
def route_set_inactive(colour='red'):
    now = datetime.now().date()
    td = timedelta(days=30)
    up_date_active = (now - td).strftime('%d/%m/%Y')
    down_date_active = (now - td).strftime('%d/%m/%Y')
    gym_and_route_set(colour=colour, up_date = up_date_active , down_date=down_date_active)

def create_sample_route_record(user_id=1,route_id=1,record_type=conf.ClimbStatus.climbed.value):
    dal.set_route_record_for_user(user_id,route_id,record_type)
