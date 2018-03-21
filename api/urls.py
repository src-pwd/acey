from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_jwt import views as jwt_views
from djoser import views as djoser_views
from .views import *

urlpatterns = {
	# url(r'^user/logout/all/$', views.SpaUserLogoutAllView.as_view(), name='user-logout-all'),
	url(r'^api/login/$', jwt_views.ObtainJSONWebToken.as_view(), name='user-login'),
	url(r'^api/login/refresh/$', jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
	url(r'^api/users/$', ProfilesView.as_view(), name="create"),
	url(r'^api/users/(?P<pk>[0-9]+)/$',
		DetailsProfileView.as_view(), name="details"),
	url(r'^api/events/$', EventsView.as_view(), name="create"),
	url(r'^api/events/(?P<pk>[0-9]+)/$',
		DetailsEventView.as_view(), name="details"),
	url(r'^api/predictions/$', PredictionsView.as_view(), name="create"),
	url(r'^api/accuratepredictions/$', AccuratePredictionsView.as_view(), name="create"),
	url(r'^api/parleyevents/$', ParleyEventsView.as_view(), name="create"),
	url(r'^api/options/$', OptionsView.as_view(), name="create"),
	url(r'^api/options/(?P<pk>[0-9]+)/$',
		DetailsOptionView.as_view(), name="details"),
	url(r'^api/bets/$', BetsView.as_view(), name="create"),
	url(r'^api/bets/(?P<pk>[0-9]+)/$',
		DetailsBetView.as_view(), name="details"),
	url(r'^api/accuratebets/$', AccurateBetsView.as_view(), name="create"),
	url(r'^api/parleys/$', ParleysView.as_view(), name="create"),
	url(r'^api/parleys/(?P<pk>[0-9]+)/$',
		DetailsParleyView.as_view(), name="details"),
}
	
urlpatterns = format_suffix_patterns(urlpatterns)