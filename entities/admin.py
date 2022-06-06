from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models import Count

from .models import *


admin.site.site_title = 'Entity Site title'
admin.site.site_header = 'Entity Site Header'
admin.site.index_title = 'Welcome, this is index header'

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Villain)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_immortal', 'category', 'origin')
    list_filter = ('is_immortal', 'category', 'origin')

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ['name', 'hero_count', 'villain_count']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count = Count('hero', distinct=True),
            _villain_count = Count('villain', distinct=True),
        )

        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count
