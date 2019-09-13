"""RPGuru Library Admin Models"""

from django.contrib import admin

from .models import Game, Platform, Franchise, Company, Genre


class PlatformAdmin(admin.ModelAdmin):
    fields = (('name', 'short', 'slug', ),
              ('artwork'),
              ('description'))
    prepopulated_fields = {'slug': ('short',)}
    list_display = ('pk', 'name', 'short', 'slug')
    list_display_links = ('pk', 'name',)
    ordering = ['pk']

    def get_readonly_fields(self, request, obj=None):
        # Image filename relies on PK, so only allow images to be added on edits
        return ['artwork'] if obj is None else []


class FranchiseAdmin(admin.ModelAdmin):
    fields = (('name', 'slug', ),
              ('artwork'),
              ('description'))
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('pk', 'name', 'slug')
    list_display_links = ('pk', 'name',)
    ordering = ['pk']

    def get_readonly_fields(self, request, obj=None):
        # Image filename relies on PK, so only allow images to be added on edits
        return ['artwork'] if obj is None else []


class CompanyAdmin(FranchiseAdmin):
    # Franchise and Company model are so similar we can reuse the Admin model
    pass


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
              ('platform', 'audio',),
              ('franchise_main', 'franchise_side',),
              ('developer', 'publisher', 'genre',),
              ('description',))
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)
    ordering = ['-date_created']

    def get_readonly_fields(self, request, obj=None):
        # Image filename relies on PK, so only allow images to be added on edits
        return ['artwork', 'date_created'] if obj is None else ['date_created']


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Franchise, FranchiseAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
