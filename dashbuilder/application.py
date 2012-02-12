from django.conf.urls import patterns, include, url 
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from dashbuilder.views import List, Create, Update


class Application(object):
    name = None
    namespace = None
    url_segment = None
    index_view = TemplateView
    index_template = None

    def __init__(self, app_name=None, **kwargs):
        if not hasattr(self, 'registry'):
            self.registry = []
        self.parent = None

        self.app_name = app_name

        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def get_index_kwargs(self):
        return {
            'template_name': self.index_template,
        }

    def register(self, app):
        self.registry.append(app)

    def get_urls(self):
        urlpatterns = patterns('')

        urlpatterns += patterns('', url(r'^$',
            self.view_wrapper(self.index_view.as_view(**self.get_index_kwargs())),
            name='index'))

        for app in self.registry:
            app.parent = self
            urlregex = r'^%s/' % app.namespace
            urlpatterns += patterns('', url(urlregex, include(app.urls)))
        return urlpatterns

    def get_root_application(self):
        if not self.parent:
            return self
        return self.parent.get_root_application()

    def get_ancestors(self):
        if not self.parent:
            return []
        ancestors = self.parent.get_ancestors()
        ancestors.append(self.parent)
        return ancestors

    def get_context_data(self, request, *args, **kwargs):
        data = {}
        data['application'] = self
        data['root_application'] = self.get_root_application()
        data['ancestor_applications'] = self.get_ancestors()
        return data

    def view_wrapper(self, view):
        def modify_context(request, *args, **kwargs):
            response = view(request, *args, **kwargs)
            if hasattr(response, 'context_data'):
                response.context_data.update(self.get_context_data(request, *args, **kwargs))
            return response
        return modify_context

    def get_url_namespace(self):
        if self.parent:
            prefix = self.parent.get_url_namespace()
        else:
            prefix = ''
        return '%s%s:' % (prefix, self.namespace)

    def get_index_url(self):
        return reverse('%sindex' % self.get_url_namespace())

    @property
    def urls(self):
        # We set the application and instance namespace here
        return self.get_urls(), self.app_name, self.namespace


class Dashboard(Application):
    name = 'Django Dashbuilder'
    namespace = 'dashboard'
    index_template = 'dashbuilder/index.html'


class Section(Application):
    index_template = 'dashbuilder/section_index.html'


class ModelApplication(Application):
    model = None
    index_view = List
    create_view = Create
    update_view = Update

    create_form = None
    update_form = None

    def get_index_kwargs(self):
        return {
            'model': self.model,
        }

    def create_view_name(self):
        return '%screate' % self.get_url_namespace()

    def update_view_name(self):
        return '%supdate' % self.get_url_namespace()

    def get_urls(self):
        urlpatterns = super(ModelApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^new/$',
                    self.view_wrapper(self.create_view.as_view(model=self.model,
                        app=self, form_class=self.create_form)), name='create'),
            url(r'^(?P<pk>[0-9]+)/$',
                self.view_wrapper(self.update_view.as_view(model=self.model, app=self,
                    form_class=self.update_form)), name='update'),
        )
        return urlpatterns

