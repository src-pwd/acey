from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Profile
from .serializers import *
from rest_framework.metadata import SimpleMetadata


class ProfilesView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAdminUser,)

class DetailsProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAdminUser,)

class EventsView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (IsAdminUser,)

class DetailsEventView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class OptionsView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = (IsAdminUser,)

class PredictionsView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(type = "Prediction")
    serializer_class = PredictionSerializer
    metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

# class DetailsPredictionView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = PredictionSerializer
#     metadata_class = SimpleMetadata
    # permission_classes = (IsAdminUser,)

class DetailsOptionView(generics.RetrieveUpdateDestroyAPIView):
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
