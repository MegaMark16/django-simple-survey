from django.conf.urls.defaults import *
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.list_surveys),
    (r'^(?P<survey_id>\d+)/$', views.take_survey),
)
