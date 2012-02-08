from django.conf.urls.defaults import patterns, include, url
from dashbuilder.views import List, Create, Update 
from django.contrib.auth.models import User

class ListUsers(List):
    model = User
    fields = ('username', 'first_name', 'last_name',)

urlpatterns = patterns('',
    url(r'^users/', ListUsers.as_view(), name='list-users'),

)
