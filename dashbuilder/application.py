from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from dashbuilder.views import List, Create, Update


class Application(object):
    name = None
    url_segment = None

    def __init__(self, app_name=None, **kwargs):
        self.app_name = app_name
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def get_urls(self):
        """
        Return the url patterns for this app, MUST be implemented in the subclass
        """
        return patterns('')

    @property
    def urls(self):
        # We set the application and instance namespace here
        return self.get_urls(), self.name, self.name


class RegistryApplication(Application):
    """
    An application that has is capable of storing sub-applications.
    Used for grouping the dashboard into sets of functionality
    """
    registry = []
    index_view = TemplateView
    index_template = 'dashbuilder/section_index.html'

    def register(self, app):
        self.registry.append(app)

    def get_urls(self):
        urlpatterns = super(RegistryApplication, self).get_urls()

        urlpatterns += patterns('', url(r'^$',
            self.index_view.as_view(template_name=self.index_template)))

        for app in self.registry:
            urlregex = r'^%s/' % app.name
            urlpatterns += patterns('', url(urlregex, include(app.urls)))
            print 'moo'
        return urlpatterns


class Dashboard(RegistryApplication):
    name = 'Django Dashbuilder'
    index_template = 'dashbuilder/index.html'


class Section(RegistryApplication):
    name = 'Group'


class ModelApplication(Application):
    model = None
    index_view = List
    create_view = Create
    update_view = Update

    create_form = None
    update_form = None

    def get_urls(self):
        print 'hi!'
        urlpatterns = super(ModelApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^$', self.index_view.as_view(model=self.model, app=self), name='index'),
            url(r'^new/$', self.create_view.as_view(model=self.model, app=self,
                form_class=self.create_form), name='create'),
            url(r'^(?P<pk>[0-9]+)/$',
                self.update_view.as_view(model=self.model, app=self,
                    form_class=self.update_form), name='update'),
        )
        return urlpatterns

