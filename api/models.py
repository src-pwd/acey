from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    profile_picture = models.FileField(null = True, blank = True)
    rate = models.IntegerField(default = 0, blank = True)
    info = models.CharField(max_length = 500, blank = True)
    sum = models.IntegerField(default = 0)
    bets = models.IntegerField(default = 0)
    events = models.IntegerField(default = 0)
    activity_rate = models.IntegerField(default = 0, blank = True)
    win_rate = models.IntegerField(default = 0, blank = True)
    jwt_secret = models.UUIDField(default=uuid.uuid4)


def jwt_get_secret_key(user_model):
    return Profile.objects.get(user = user_model).jwt_secret


class Event(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator")
    name = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20, default = "New")
    type = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add = True)
    expired = models.DateTimeField()
    description = models.CharField(max_length = 500)
    currency_pair = models.CharField(max_length = 10)
    exchange = models.CharField(max_length = 30)
    total_users = models.IntegerField(default = 0)
    total_sum = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id) + ": " + self.name

class Parley(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "parleys")
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "parley_creator")
    bettor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "parley_bettor", null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    koefficient = models.FloatField()
    min_sum = models.IntegerField()
    max_sum = models.IntegerField()
    status = models.CharField(max_length = 20)
    bet_sum = models.IntegerField(null = True)

class Option(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "options")
    total_users = models.IntegerField(default = 0)
    total_sum = models.IntegerField(default = 0)
    sum_from = models.IntegerField()
    sum_to = models.IntegerField()

    def __str__(self):
        return str(self.id) + ": " + str(self.sum_from) + "-" + str(self.sum_to) + " in " + str(self.event.id) + ": " + self.event.name

class Bet(models.Model):
    option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = "bet_option")
    bettor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "bet_user")
    sum = models.IntegerField()

class AccurateBet(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "accurate_bet_event")
    bettor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "accurate_bet_user")
    sum = models.IntegerField()
    stake = models.IntegerField()

class Currencies(models.Model):
    name = models.CharField(max_length = 11, primary_key = True)

    def __str__(self):
        return str(self.name)

class Exchange(models.Model):
    name = models.CharField(max_length = 40)
    url = models.CharField(max_length = 100)
    currencies = models.ManyToManyField(Currencies, through = "ExchangeCurrencies")

class ExchangeCurrencies(models.Model):
    exchange = models.ForeignKey(Exchange)
    currencies = models.ForeignKey(Currencies)










