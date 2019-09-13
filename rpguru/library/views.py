"""RPGuru Library views"""

from django.views.generic.detail import DetailView

from .models import Platform, Franchise, Company, Genre


class PlatformDetailView(DetailView):
    template_name = 'library/platform.html'
    model = Platform


class FranchiseDetailView(DetailView):
    template_name = 'library/franchise.html'
    model = Franchise


class CompanyDetailView(DetailView):
    template_name = 'library/company.html'
    model = Company


class GenreDetailView(DetailView):
    template_name = 'library/genre.html'
    model = Genre
