import csv
with open("merge_yes.csv", "r") as f:
	first = {rows[0]: rows[1:] for rows in list(csv.reader(f))}
	#creating a dictionary with house id as key and remaing features as values

with open("house_prices.csv", "r") as f:
	for row in csv.reader(f):
		if row[0] in first:			#if house id present in house_prices.csv(training data),append golden_grains feature to corresponding house id key
			first[row[0]].append(row[1])
			
#converting dictionary back to list
merged = [(k,) + tuple(v) for k, v in first.items()]

with open("train.csv", "w") as f:			#first dictionary contains all training data ,write to train.csv
									#refer to csv_separating.py
    csv.writer(f).writerows(merged)
