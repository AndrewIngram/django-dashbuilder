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


class Group1(Section):
    name = 'group1'
    registry = [
        UsersApplication(name='users')
    ]


class Group2(Section):
    name = 'group2'
    registry = [
        ModelApplication(model=Redirect, name='redirects'),
        ModelApplication(model=Site, name='sites'),
    ]


dashboard = Dashboard(name='Dashboard Demo')
dashboard.register(UsersApplication(name='users'))
dashboard.register(Group2)

urlpatterns = patterns('',
    url(r'^', include(dashboard.urls)),
)

