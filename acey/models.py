from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 64)
	email = models.CharField(max_length = 50)
	user_picture = models.ImageField(null = True, blank = True)
	rate = models.IntegerField()
	created = models.DateField(auto_now_add = True)
	info = models.TextField(max_length = 500, blank = True)
	name = models.CharField(max_length = 50, blank = True)
	sum = models.IntegerField()
	bets = models.IntegerField()
	events = models.SmallIntegerField()
	activity_rate = models.IntegerField()
	win_rate = models.IntegerField()

class Event(models.Model):
	creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "event_creator")
	name = models.CharField(max_length = 100)
	status = models.CharField(max_length = 20)
	type = models.CharField(max_length = 20)
	created = models.DateTimeField(auto_now_add = True)
	expired = models.DateTimeField()
	description = models.TextField(max_length = 500)
	currency_pair = models.CharField(max_length = 10)
	exchange = models.CharField(max_length = 30)
	total_users = models.IntegerField()
	total_sum = models.IntegerField()

class EventParley(models.Model):
	event = models.OneToOneField(Event, on_delete = models.CASCADE, related_name = "event_parley")

class Parley(models.Model):
	event = models.ForeignKey(EventParley, on_delete = models.CASCADE, related_name = "parley_event")
	creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "parley_creator")
	bettor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "parley_bettor", null = True)
	created = models.DateTimeField(auto_now_add = True)
	koefficient = models.FloatField()
	min_sum = models.IntegerField()
	max_sum = models.IntegerField()
	status = models.CharField(max_length = 20)
	bet_sum = models.IntegerField(null = True)

class Prediction(models.Model):
	event = models.OneToOneField(Event, on_delete = models.CASCADE, related_name = "prediction_event")

class Option(models.Model):
	prediction = models.ForeignKey(Prediction, on_delete = models.CASCADE, related_name = "option_prediction")
	total_users = models.IntegerField()
	total_sum = models.IntegerField()
	sum_from = models.IntegerField()
	sum_to = models.IntegerField()

class Bet(models.Model):
	option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = "bet_option")
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "bet_user")
	sum = models.IntegerField()

class AccuratePrediction(models.Model):
	event = models.OneToOneField(Event, on_delete = models.CASCADE, related_name = "accurate_prediction_event")

class AccurateBet(models.Model):
	prediction = models.ForeignKey(AccuratePrediction, on_delete = models.CASCADE, related_name = "accurate_bet_prediction")
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "accurate_bet_user")
	sum = models.IntegerField()
	stake = models.IntegerField()











