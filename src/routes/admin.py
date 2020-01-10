from django.contrib import admin

# Register your models here.
from routes.models import Gym, Route, RouteSet, RouteRecord

admin.site.register(Gym)
admin.site.register(Route)
admin.site.register(RouteSet)
admin.site.register(RouteRecord)
