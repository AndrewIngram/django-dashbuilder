from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.sites.models import Site

from dashbuilder.application import ModelApplication


class UsersApplication(ModelApplication):
    model = User
    create_form = UserCreationForm
    update_form = UserChangeForm


urlpatterns = patterns('',
    url(r'^users/', include(UsersApplication().urls)),
    url(r'^redirects/', include(ModelApplication(model=Redirect, name='redirects').urls)),
    url(r'^sites/', include(ModelApplication(model=Site, name='sites').urls))
)

