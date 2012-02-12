from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.sites.models import Site

from dashbuilder.application import Dashboard, Section, ModelApplication
from dashbuilder.views import Create


class UsersApplication(ModelApplication):
    model = User
    create_form = UserCreationForm
    update_form = UserChangeForm


class Group(Section):
    name = 'Group'
    namespace = 'group'
    registry = [
        ModelApplication(model=Redirect, name='Redirects', namespace='redirects'),
        ModelApplication(model=Site, name='Sites', namespace='sites'),
    ]


dashboard = Dashboard(namespace='dashboard', name='Dashboard Demo')
dashboard.register(UsersApplication(name='Users', namespace='users'))
dashboard.register(Group())

urlpatterns = patterns('',
    url(r'^', include(dashboard.urls)),
)

