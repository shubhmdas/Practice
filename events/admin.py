from django.contrib import admin


from .models import *


class EventAdminSite(admin.AdminSite):
    site_title = 'Event Site title'
    site_header = 'Event Site Header'
    index_title = 'Welcome, this is index header'

event_admin_site = EventAdminSite(name='event_admin')


event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)
