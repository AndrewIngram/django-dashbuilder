from extra_views import ModelFormSetView, CreateWithInlinesView, UpdateWithInlinesView 


class ListTemplateResponseMixin(object):
    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if get_template is overridden.
        """
        try:
            names = super(ChangeList, self).get_template_names()
        except ImproperlyConfigured:
            # If template_name isn't specified, it's not a problem --
            # we just start with an empty list.
            names = []

        # If the list is a queryset, we'll invent a template name based on the
        # app and model name. This name gets put at the end of the template
        # name list so that user-supplied names override the automatically-
        # generated ones.
        if hasattr(self.object_list, 'model'):
            opts = self.object_list.model._meta
            names.append("dashbuilder/%s/%s%s.html" % (opts.app_label, opts.object_name.lower(), self.template_name_suffix))
        return names


class DetailTemplateResponseMixin(object):
    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if get_template is overridden.
        """
        try:
            names = super(DetailTemplateResponseMixin, self).get_template_names()
        except ImproperlyConfigured:
            # If template_name isn't specified, it's not a problem --
            # we just start with an empty list.
            names = []

        # If self.template_name_field is set, grab the value of the field
        # of that name from the object; this is the most specific template
        # name, if given.
        if self.object and self.template_name_field:
            name = getattr(self.object, self.template_name_field, None)
            if name:
                names.insert(0, name)

        # The least-specific option is the default <app>/<model>_detail.html;
        # only use this if the object in question is a model.
        if hasattr(self.object, '_meta'):
            names.append("%s/%s%s.html" % (
                self.object._meta.app_label,
                self.object._meta.object_name.lower(),
                self.template_name_suffix
            ))
        elif hasattr(self, 'model') and hasattr(self.model, '_meta'):
            names.append("%s/%s%s.html" % (
                self.model._meta.app_label,
                self.model._meta.object_name.lower(),
                self.template_name_suffix
            ))
        return names


class ChangeList(ListTemplateResponseMixin, ModelFormSetView):
    pass


class CreateView(DetailTemplateResponseMixin, CreateWithInlinesView):
    pass


class UpdateView(DetailTemplateResponseMixin, UpdateWithInlinesView):
    pass


