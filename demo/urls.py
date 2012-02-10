from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.sites.models import Site

from dashbuilder.application import Dashboard, RegistryApplication, ModelApplication
from dashbuilder.views import Create


class UsersApplication(ModelApplication):
    model = User
    create_form = UserCreationForm
    update_form = UserChangeForm


class Group(RegistryApplication):
    name = 'group'
    registry = [
        ModelApplication(model=Redirect, name='redirects'),
        ModelApplication(model=Site, name='sites'),
    ]


dashboard = Dashboard(name='Dashboard Demo')
dashboard.register(UsersApplication(name='users'))
dashboard.register(Group())

urlpatterns = patterns('',
    url(r'^', include(dashboard.urls)),
)

