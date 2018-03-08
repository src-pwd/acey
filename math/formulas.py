
def refund(d, p):
	l = {}
	sums = {}
	for j,i in d.items():
		k = abs(p-i[0])/p
		k = 100 * k if k>0.00001 else 0.001
		l[j] = round((i[1]/k) - 0.0005, 3)

	total = sum([x[1] for x in d.values()])
	part = total/sum(l.values())
	for j, i in l.items():
		sums[j] = i*part
		sums[j] = int(sums[j]) if sums[j] - int(sums[j]) < 0.6 else int(sums[j])+1
	return sums

	# result = []
	# for i in d.keys():
	# 	result.append({"Stake": d[i][0], "Sum": d[i][1], "Refund": sums[i]})
	# print(total)
	# print(sum([x["Refund"] for x in result]))
	# return sorted(result, key = lambda x: abs(p - x["Stake"]))