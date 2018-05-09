# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import sys
# import datetime
# import os
# import requests
# import json
# from django.db import transaction
# sys.path.append('..')
# from api.models import *

# EXCHANGE_FEE = 3

# def refund(d, p):
# 	l = {}
# 	sums = {}
# 	for j,i in d.items():
# 		k = abs(p-i[0])/p
# 		k = 100 * k if k>0.00001 else 0.001
# 		l[j] = round((i[1]/k) - 0.0005, 3)

# 	total = sum([x[1] for x in d.values()])
# 	part = total/sum(l.values())
# 	for j, i in l.items():
# 		sums[j] = i*part
# 		sums[j] = int(sums[j]) if sums[j] - int(sums[j]) < 0.6 else int(sums[j])+1
# 	return sums

# exchange = sys.argv[1]
# # currency_pair = sys.argv[2]
# currency_from = sys.argv[2][:3]
# currency_to = sys.argv[2][4:]
# event_id = sys.argv[3]
# event_type = sys.argv[4]

# SYMBOLS = ['tBTCUSD', 'tETHUSD', 'tLTCUSD', 'tDSHUSD', 'tXMRUSD']

# if ("t"+currency_from.upper()+"USD") in SYMBOLS:
# 	if ("t"+currency_to.upper()+"USD") in SYMBOLS or currency_to.upper()=="USD":

# 		symbols_query = ','.join(SYMBOLS)
# 		req = requests.get("https://api.bitfinex.com/v2/tickers?symbols={}".format(symbols_query), headers = {"Content-Type": "application/json; charset=utf-8"})
# 		resp = json.loads(req.text)
# 		data = {}
# 		for val in resp:
# 			data[val[0]] = val[7]

# 		result = data.get("t"+currency_from.upper()+"USD")/data.get("t"+currency_to.upper()+"USD") if currency_to.upper()!="USD" else data.get("t"+currency_from.upper()+"USD")
# 	else:
# 		pass
# else:
# 	pass

# if event_type == "Prediction":
# 	with transaction.atomic():
# 		options = Option.objects.filter(event__id = event_id)
# 		bets = Bet.objects.filter(option__event__id = event_id)
# 		options_values = options.values()
# 		option_win_id = 0
# 		for index in range(len(options)):
# 			if index==0:
# 				if result<=options_values[index]['sum_to']:
# 					break
# 			elif index==len(options)-1:
# 				if result>=options_values[index]['sum_from']:
# 					option_win_id = index
# 			else:
# 				if result>=options_values[index]['sum_from'] and result>=options_values[index]['sum_from']:
# 					option_win_id = index
# 		win_user_set = []
# 		for bet in 






