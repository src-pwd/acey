from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
	url(r'^users/$', ProfilesView.as_view(), name="create"),
	url(r'^users/(?P<pk>[0-9]+)/$',
		DetailsProfileView.as_view(), name="details"),
	url(r'^events/$', EventsView.as_view(), name="create"),
	url(r'^events/(?P<pk>[0-9]+)/$',
		DetailsEventView.as_view(), name="details"),
	url(r'^predictions/$', PredictionsView.as_view(), name="create"),
	url(r'^predictions/(?P<pk>[0-9]+)/$',
		DetailsPredictionView.as_view(), name="details"),
	url(r'^options/$', OptionsView.as_view(), name="create"),
	url(r'^options/(?P<pk>[0-9]+)/$',
		DetailsOptionView.as_view(), name="details"),
	url(r'^bets/$', BetsView.as_view(), name="create"),
	url(r'^bets/(?P<pk>[0-9]+)/$',
		DetailsBetView.as_view(), name="details"),
	url(r'^accuratebets/$', AccurateBetsView.as_view(), name="create"),
	url(r'^parleys/$', ParleysView.as_view(), name="create"),
	url(r'^parleys/(?P<pk>[0-9]+)/$',
		DetailsParleyView.as_view(), name="details"),
}
	
urlpatterns = format_suffix_patterns(urlpatterns)