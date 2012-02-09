from django.conf.urls.defaults import patterns, include, url
from dashbuilder.views import List, Create, Update


class Application(object):
    name = None

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
        return self.get_urls(), self.app_name, self.name


class ModelApplication(Application):
    model = None
    index_view = List
    create_view = Create
    update_view = Update

    create_form = None
    update_form = None

    def get_urls(self):
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

