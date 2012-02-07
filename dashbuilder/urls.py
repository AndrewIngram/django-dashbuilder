from django.conf.urls.defaults import url, patterns, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='admin2/index.html'), name='admin2-index'),
)
