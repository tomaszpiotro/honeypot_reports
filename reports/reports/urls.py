from django.conf.urls import patterns, url
from reports.views import ReportsView, ReportDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', ReportDetailView.as_view()),
    url(r'^$', ReportsView.as_view()),
    )
