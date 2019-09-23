"""RPGuru Library views"""

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Platform, Franchise, Company, Genre, Game


class PlatformDetailView(DetailView):
    template_name = 'library/platform.html'
    model = Platform

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.filter(platform=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        return context


class FranchiseDetailView(DetailView):
    template_name = 'library/franchise.html'
    model = Franchise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Main games
        context['main'] = Game.objects.filter(franchise_main=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        # Side games
        context['side'] = Game.objects.filter(franchise_side=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        return context


class CompanyDetailView(DetailView):
    template_name = 'library/company.html'
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Games developed
        context['developed'] = Game.objects.filter(developer=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        # Games published
        context['published'] = Game.objects.filter(publisher=context['object'])\
            .exclude(developer=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        return context


class GenreDetailView(DetailView):
    template_name = 'library/genre.html'
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.filter(genre=context['object'])\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')
        return context


class FrontpageView(TemplateView):
    template_name = 'frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()\
            .select_related('franchise_main', 'franchise_side')\
            .prefetch_related('audio', 'developer', 'publisher', 'genre', 'platform')\
            .order_by('-na_date', '-jp_date', '-eu_date')[0:5]
        return context
