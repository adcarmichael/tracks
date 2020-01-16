from django.contrib import admin

# Register your models here.
from routes.models import Gym, Route, RouteSet, RouteRecord, Zone

admin.site.register(Gym)
admin.site.register(Route)
admin.site.register(RouteRecord)
admin.site.register(Zone)


class RoutesInline(admin.TabularInline):
    model = Route


class RouteSetAdmin(admin.ModelAdmin):
    inlines = [
        RoutesInline,
    ]


admin.site.register(RouteSet, RouteSetAdmin)
