import csv
import pandas as pd
fhand = open('Bob.txt')			#open the text file to parse data
count =1						#total 19 features ,some features might be missing however between each house info there are two empty lines
data = []						#store each house details in data[] and append them to mult[]
mult = []
for line in fhand:
	if count == 20 or count == 21:	#every 20th,21st line will be empty
		count =1				#for every %22 line make count =1	
		mult.append(data)		
		data = []
		continue					#because 20,21 lines are empty
	line = line.rstrip()				#remove the newline 
	#print(line)
#1	
	if count == 1:
		if line.startswith('House'):		#feature 1 starts with house 	
			z = line.split(':')			#we need house id ,split the line and store house id		
			data.append(z[1].strip())
			count += 1				#increment count
			continue					#skip remaining part we got what we want,move to next line
#2	
	if count == 2:
		if line.startswith('Date'):		#feature 2 starts with date 
			y = line.split(' ')
			data.append(y[3]+" "+y[4]+" "+y[5])		#storing date , time for house built 			
			data.append(y[11]+" "+y[12]+" "+y[13])	#storing date , time for house priced
			count += 1				#increment count
			continue					#skip remaining part we got what we want,move to next line
#3		
	if count == 3:
		if line.startswith('There '):  	#feature 3 starts with There
			if 'no' in line:			#categorical data (yes(1) or no(0) ),if data missing append empty string
				data.append(0)
				count += 1
				continue
			else:
				#print(line)
				data.append(1)
				count += 1
				continue
		else:
			data.append('')
			count += 1
			
#4
	if count == 4:
		if line.startswith('Distance from the Dock'):	#feature 4 starts with Distance
			for i in line.split():			#the entire strings contains a float value and all other strings(will give exception,catch them and continue ) 
				try:
					result = float(i)
					break			#break inner for lop after getting your required float value
				except:
					continue
			data.append(result)
			count += 1
			continue
		else:
				data.append('')
				count += 1
					
		
#5	
	if count == 5:
		if line.startswith('Distance from Capital'):	#feature 5 starts with Distance
			for i in line.split():			#the entire strings contains a float value and all other strings(will give exception,catch them and continue )
				try:
					result = float(i)	#break inner for lop after getting your required float value
					break
				except:
					continue
			data.append(result)
			count += 1
			continue
		else:
				data.append('')
				count += 1
					
	
#6		
	if count == 6:
		if line.startswith('Distance from Royal Market'):	#feature 5 starts with Distance
			for i in line.split():				#the entire strings contains a float value and all other strings(will give exception,catch them and continue )
				try:
					result = float(i)		#break inner for lop after getting your required float value
					break
				except:
					continue
			data.append(result)
			count += 1	
			continue	
		else:
				data.append('')
				count += 1
					
	
#7
	if count == 7:
		if line.startswith('Distance from Guarding Tower'):	#feature  starts with Distance
			for i in line.split():			#the entire strings contains a float value and all other strings(will give exception,catch them and continue )
				try:
					result = float(i)	#break inner for lop after getting your required float value
					break
				except:
					continue
			data.append(result)
			count += 1
			continue	
		else:
				data.append('')
				count += 1
					
	
#8
	if count == 8:
		if line.startswith('Distance from the River'):	#feature  starts with Distance
			for i in line.split():
				try:
					result = float(i)	#break inner for lop after getting your required float value
					break
				except:
					continue
			data.append(result)
			count += 1
			continue
		else:
				data.append('')		#if line missing add empty string
				count += 1
					
		
#9		
	if count == 9:
		if line.startswith('The house') :  
			if 'not' in line:
				data.append(0)		#categorical data (yes(1) or no(0) ),if data missing append empty string
				count += 1
				continue
			else:
				data.append(1)
				count += 1
				continue
		else:
				data.append('')
				count += 1
				
	
#10
	if count == 10:
		if line.startswith('There ') and line.endswith('dining rooms'):
			data.extend(int(s) for s in line.split() if s.isdigit())
			count += 1			#find the digit in string and append it ,if line missing add empty string
			continue
		else:
				data.append('')
				count += 1
				
	
#11
	if count == 11:
		if line.startswith('There ') and line.endswith('bedrooms'):
			data.extend(int(s) for s in line.split() if s.isdigit())
			count += 1		#find the digit in string and append it ,if line missing add empty string
			continue
		else:
				data.append('')
				count += 1
				
		
#12
	if count == 12:
		if line.startswith('There ') and line.endswith('bathrooms'):
			data.extend(int(s) for s in line.split() if s.isdigit())
			count += 1
			continue			#find the digit in string and append it ,if line missing add empty string
		else:
				data.append('')
				count += 1
				
	
#13
	if count == 13:
		if (line.startswith('King ') and line.endswith('house')) or (line.startswith('The ')):  
			if line.startswith('King'):
				data.append(0)
				count += 1
				continue
			else:				#categorical data (yes(1) or no(0) ),if data missing append empty string
				data.append(1)
				count += 1
				continue
		else:
			data.append('')
			count += 1
				
	
#14
	if count == 14:
		if line.startswith('Sorcerer') or line.startswith('This') :  
			if 'couldn\'t' in line:
				data.append(0)
				count += 1
				continue
			else:
				data.append(1)			#categorical data (yes(1) or no(0) ),if data missing append empty string
				count += 1
				continue
		else:
				data.append('')
				count += 1
				
	
#15
	if count == 15:
		if line.startswith('King') and line.endswith('blessings'):
			data.extend(int(s) for s in line.split() if s.isdigit())
			count += 1
			continue
		else:
				data.append('')
				count += 1
					
	
#16
	if count == 16:
		if line.startswith('There'):  
				xy = line.split(' ')
				if 'front' in line:
					data.append(xy[3]+" "+xy[4])
				else:
					data.append(xy[2]+" "+xy[3])
				count += 1
				continue
		else:
				data.append('')
				count += 1
					
	
#17
	if count == 17:
		if line.startswith('Location'):	
			x = line.split(':')
			data.append(x[1].strip())	#location is specified after : ,so split the string and add the 2nd string(index 1) to data  
			count += 1
			continue
		else:
				data.append('')
				count += 1
				
	
#18
	if count == 18:
		if line.startswith('Holy tree stands tall beside the house'):
			data.append(1)
			count += 1
			continue					#categorical data (yes(1) or no(0) ),if data missing append empty string
		elif line.startswith('Holy tree was cut to death by Ancient Witch'):
			data.append(0)
			count += 1
			continue
		else:
				data.append('')
				count += 1
				
	
	
#19
	if count == 19:
		if line.startswith('Distance') and line.endswith('holy lights'):
			for i in line.split(' '):
				try:
					result = float(i)
					break
				except:
					continue				#the entire strings contains a float value and all other strings(will give exception,catch them and continue )
			data.append(result)
			import numpy as np 
			count += 1
			continue
		else:
				data.append(' ')
				count += 1
						
		

#creating a writer object and writing to file row wise from mult[], 2nd parameter is the named of corresponding builder
with open("Bob.csv", "w") as f:
	writer = csv.writer(f,delimiter=',')
	ps = ['House ID','Builder Name','Date Built','Date Priced','garden','Dock','Capital','Royal Market','Guarding Tower','River','renovation','dining rooms','bedrooms','bathrooms','visit','Sorcerer','blessings','land','Location','Holy tree','Knight\'s house']
	writer.writerow(ps)
	for sublist in mult:
			writer.writerow([sublist[0],'Bob',sublist[1],sublist[2],sublist[3],sublist[4],sublist[5],sublist[6],sublist[7],sublist[8],sublist[9],sublist[10],sublist[11],sublist[12],sublist[13],sublist[14],sublist[15],sublist[16],sublist[17],sublist[18],sublist[19]])
	
	

