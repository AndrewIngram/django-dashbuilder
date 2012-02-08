from django.conf.urls.defaults import patterns, include, url
from dashbuilder.views import List, Create, Update 
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ListUsers(List):
    model = User
    fields = ('username', 'first_name', 'last_name',)


class CreateUser(Create):
    model = User
    form_class = UserCreationForm


class UpdateUser(Update):
    model = User
    form_class = UserChangeForm


class ListRedirects(List):
    model = Redirect


class CreateRedirect(Create):
    model = Redirect


urlpatterns = patterns('',
    url(r'^users/$', ListUsers.as_view(), name='list-users'),
    url(r'^users/new/$', CreateUser.as_view(), name='create-user'),
    url(r'^users/(?P<pk>[0-9]+)/$', UpdateUser.as_view(), name='update-user'),
    url(r'^redirects/$', ListRedirects.as_view(), name='list-redirects'),
    url(r'^redirects/new/$', CreateRedirect.as_view(), name='create-redirect'),
)    

