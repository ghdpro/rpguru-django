"""RPGuru Library Admin Models"""

from django.contrib import admin

from .models import Game, Platform, Franchise, Company, Genre


class PlatformAdmin(admin.ModelAdmin):
    fields = (('name', 'slug', ),
              ('artwork'),
              ('description'))
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)
    ordering = ['pk']

    def get_readonly_fields(self, request, obj=None):
        # Image filename relies on PK, so only allow images to be added on edits
        return ['artwork'] if obj is None else []


class GenreAdmin(admin.ModelAdmin):
    fields = (('name', 'slug', ),
              ('description'))
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)
    ordering = ['pk']


class GameAdmin(admin.ModelAdmin):
    fields = (('title', 'verdict',),
              ('artwork',),
              ('jp_date', 'na_date', 'eu_date',),
              ('audio',),
              ('franchise_main', 'franchise_side',),
              ('platform', 'developer', 'publisher', 'genre',),
              ('description',))
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)
    ordering = ['-date_created']

    def get_readonly_fields(self, request, obj=None):
        # Image filename relies on PK, so only allow images to be added on edits
        return ['artwork', 'date_created'] if obj is None else ['date_created']


admin.site.register(Platform, PlatformAdmin)
# The following two models are so similar we can reuse the Admin model
admin.site.register(Franchise, PlatformAdmin)
admin.site.register(Company, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
