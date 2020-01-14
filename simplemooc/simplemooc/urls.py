from django.conf.urls import patterns, include, url
from django.contrib import admin

# Servir media
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)