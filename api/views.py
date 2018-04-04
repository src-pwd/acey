import jwt,json
from django.http import HttpResponse
from rest_framework import generics, views
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import *
from .models import Profile
from .serializers import *
from rest_framework.metadata import SimpleMetadata
from django.template.loader import render_to_string

# from .permissions import IsOwner

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Accepted', status=202)
#     else:
#         return HttpResponse('Unauthorized', status=401)

class ProfilesView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]

class DetailsProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.delete()
        return HttpResponse(status=200)

class EventsView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (IsOwner,)

class DetailsEventView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsOwner,)

class OptionsView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = (IsAdminUser,)

class PredictionsView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(type = "Prediction")
    serializer_class = PredictionSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class AccuratePredictionsView(generics.ListAPIView):
    queryset = Event.objects.filter(type = "AccuratePrediction")
    serializer_class = EventSerializer
    # metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

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

class DetailsBetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    # permission_classes = (IsAdminUser,)

class AccurateBetsView(generics.ListCreateAPIView):
    queryset = AccurateBet.objects.all()
    serializer_class = AccurateBetSerializer
    # permission_classes = (IsAdminUser,)

class ParleysView(generics.ListCreateAPIView):
    queryset = Parley.objects.all()
    serializer_class = ParleySerializer
    # permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            setattr(serializer_class.Meta, 'read_only_fields', ('bettor', 'bet_sum', 'status', ))
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
