from extra_views import ModelFormSetView, CreateWithInlinesView, UpdateWithInlinesView 
from django.views.generic import ListView

class ModelViewMixin(object):
    verbose_name = None
    verbose_name_plural = None
    app = None

    def get_context_data(self, **kwargs):
        context = super(ModelViewMixin, self).get_context_data(**kwargs)

        if self.verbose_name is None:
            context['verbose_name'] = self.model._meta.verbose_name
        else:
            context['verbose_name'] = self.verbose_name
        if self.verbose_name_plural is None:
            context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        else:
            context['verbose_name_plural'] = self.verbose_name_plural
        return context


class List(ModelViewMixin, ListView):

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        names = [
            'dashbuilder/update_list.html',
        ]

        if hasattr(self.object_list, 'model'):
            opts = self.object_list.model._meta
            names.insert(0, "dashbuilder/%s/update_list.html" % (opts.app_label))
            names.insert(0, "dashbuilder/%s/%s/update_list.html" % (opts.app_label, opts.object_name.lower()))
        return names


class Create(ModelViewMixin, CreateWithInlinesView):
    inlines = []

    def get_template_names(self):
        names = [
            'dashbuilder/create_form.html',
        ]

        if hasattr(self.object, '_meta'):
            names.insert(0, "dashbuilder/%s/create_form.html" %
                    (self.object._meta.app_label))
            names.insert(0, "dashbuilder/%s/%s/create_form.html" %
                (self.object._meta.app_label,
                    self.object._meta.object_name.lower()))
        elif hasattr(self, 'model') and hasattr(self.model, '_meta'):
            names.insert(0, "dashbuilder/%s/create_form.html" %
                    (self.model._meta.app_label))
            names.insert(0, "dashbuilder/%s/%s/create_form.html" %
                (self.model._meta.app_label,
                    self.model._meta.object_name.lower()))
        return names


class Update(ModelViewMixin, UpdateWithInlinesView):
    inlines = []

    def get_template_names(self):
        names = [
            'dashbuilder/update_form.html',
        ]

        if hasattr(self.object, '_meta'):
            names.insert(0, "dashbuilder/%s/update_form.html" %
                    (self.object._meta.app_label))
            names.insert(0, "dashbuilder/%s/%s/update_form.html" %
                    (self.object._meta.app_label,
                        self.object._meta.object_name.lower()))
        elif hasattr(self, 'model') and hasattr(self.model, '_meta'):
            names.insert(0, "dashbuilder/%s/update_form.html" %
                    (self.model._meta.app_label))
            names.insert(0, "dashbuilder/%s/%s/update_form.html" %
                    (self.model._meta.app_label,
                        self.model._meta.object_name.lower()))
        return names



