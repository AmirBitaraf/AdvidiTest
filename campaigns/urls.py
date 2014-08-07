from django.conf.urls import patterns, include, url
from campaigns.views import campaigns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
		(r'^campaigns/(?P<campaign_id>\d+)',campaigns),
)

urlpatterns += staticfiles_urlpatterns()
