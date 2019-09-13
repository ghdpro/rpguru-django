"""RPGuru URL Configuration"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib import admin

from .library.views import PlatformDetailView, FranchiseDetailView, CompanyDetailView, GenreDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/<slug:slug>', PlatformDetailView.as_view(), name='platform'),
    path('series/<slug:slug>', FranchiseDetailView.as_view(), name='franchise'),
    path('company/<slug:slug>', CompanyDetailView.as_view(), name='company'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='genre'),
    path('', TemplateView.as_view(template_name='frontpage.html'), name='frontpage')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))] + \
                   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
