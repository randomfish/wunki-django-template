from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

def ping(request):
    return HttpResponse("pong", content_type="text/plain")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),                       
    url(r'^admin/', include(admin.site.urls)),

    # Simple ping-pong function which can be used in load balancers                   
    (r'^ping$', ping),
)

# Serve media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add 500 and 404 page when debugging so we know how to style it.
if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^500.html$', 'django.views.defaults.server_error'),
        (r'^404.html$', TemplateView.as_view(template_name='404.html')),
    ) + urlpatterns
