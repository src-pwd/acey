import jwt
import json
from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics, views, status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import *
from .models import Profile
from .serializers import *
from rest_framework.metadata import SimpleMetadata
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from rest_framework_jwt.views import JSONWebTokenAPIView
from .customjwt.serializer import RefreshJSONWebTokenIsActiveSerializer
from .permissions import BetOnEvent
from rest_framework.decorators import list_route

LIMIT = 20

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
        print(e)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class UserLogoutAllView(views.APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = request.data.get("token")
        except Exception as e:
            return HttpResponse("No token field in request")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, verify = False)
        except:
            return HttpResponse("Can't decode token.")
        username = payload.get("username")
        if username:
            user = User.objects.get(username = username)
            if user:
                profile = Profile.objects.get(user = user)
            profile.jwt_secret = uuid.uuid4()
            profile.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RefreshJSONWebToken(JSONWebTokenAPIView):
    serializer_class = RefreshJSONWebTokenIsActiveSerializer


class ProfilesView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]

class LeaderBoard(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by("-win_rate")
    serializer_class = ProfileSerializer

class DetailsProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.delete()
        return HttpResponse(status=200)

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class EventsView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    # permission_classes = (IsOwner,)

    def get_queryset(self):
        limit = self.request.query_params.get('limit', LIMIT)
        try:
            top_limit = abs(int(limit))
        except:
            top_limit = LIMIT
        bottom_limit = top_limit - LIMIT if top_limit > LIMIT else 0
        queryset = Event.objects.all().order_by('-id')[bottom_limit:top_limit]
        return queryset

class DetailsEventView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    metadata_class = SimpleMetadata
    permission_classes = (BetOnEvent,)

class OptionsView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Option.objects.all()
        event = self.request.query_params.get('event', None)
        if event is not None:
            queryset = queryset.filter(event__id=event)
        return queryset

class PredictionsView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(type = "Prediction")
    serializer_class = PredictionSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class AccuratePredictionsView(generics.ListAPIView):
    queryset = Event.objects.filter(type = "AccuratePrediction")
    serializer_class = EventSerializer
    # metadata_class = SimpleMetadata
    # permission_classes = (,)

class AccuratePredictionDetailsView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.filter(type = "AccuratePrediction")
    serializer_class = EventSerializer
    # metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class ParleyEventsView(generics.ListAPIView):
    queryset = Event.objects.filter(type = "Parley")
    serializer_class = EventSerializer
    # metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class ParleyEventDetailsView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.filter(type = "Parley")
    serializer_class = EventSerializer
    # metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class DetailsOptionView(generics.RetrieveDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class BetsView(generics.ListCreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Bet.objects.all()
        event = self.request.query_params.get('event', None)
        if event:
            queryset = queryset.filter(option__event__id=event)   
        else:
            option = self.request.query_params.get('option', None)
            if option:
                queryset = queryset.filter(option__id=option)
        return queryset

class DetailsBetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    # permission_classes = (IsAdminUser,)

class AccurateBetsView(generics.ListCreateAPIView):
    queryset = AccurateBet.objects.all()
    serializer_class = AccurateBetSerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = AccurateBet.objects.all()
        event = self.request.query_params.get('event', None)
        if event:
            queryset = queryset.filter(event__id=event)
        return queryset

class ParleysView(generics.ListCreateAPIView):
    queryset = Parley.objects.all()
    serializer_class = ParleySerializer
    # permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            setattr(serializer_class.Meta, 'read_only_fields', ('bettor', 'bet_sum', 'status', ))
        return serializer_class

class ReadyParleysView(generics.ListAPIView):
    serializer_class = ParleySerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        limit = self.request.query_params.get('limit', LIMIT)
        try:
            top_limit = abs(int(limit))
        except:
            top_limit = LIMIT
        bottom_limit = top_limit - LIMIT if top_limit > LIMIT else 0
        queryset = Parley.objects.filter(status = "Ready")
        event = self.request.query_params.get('event', None)
        if event is not None:
            queryset = queryset.filter(event__id=event)[bottom_limit:top_limit]
        return queryset

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            setattr(serializer_class.Meta, 'read_only_fields', tuple())
        return serializer_class

class WaitingParleysView(generics.ListAPIView):
    serializer_class = ParleySerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        limit = self.request.query_params.get('limit', LIMIT)
        try:
            top_limit = abs(int(limit))
        except:
            top_limit = LIMIT
        bottom_limit = top_limit - LIMIT if top_limit > LIMIT else 0
        queryset = Parley.objects.filter(status = "Waiting")
        event = self.request.query_params.get('event', None)
        if event is not None:
            queryset = queryset.filter(event__id=event)[bottom_limit:top_limit]
        return queryset

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            setattr(serializer_class.Meta, 'read_only_fields', tuple())
        return serializer_class

class DetailsParleyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parley.objects.all()
    serializer_class = ParleySerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method in ['PUT', 'PATCH']:
            setattr(serializer_class.Meta, 'read_only_fields', ('min_sum', 'max_sum', 'creator', 'event', 'koefficient', 'status', ))
        return serializer_class
    # permission_classes = (IsAdminUser,)

class ExchangeView(generics.ListAPIView):
    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()

class CurrenciesView(generics.ListAPIView):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()

class ExchangeCurrenciesView(generics.ListAPIView):
    serializer_class = ExchangeCurrenciesSerializer
    queryset = ExchangeCurrencies.objects.all()





