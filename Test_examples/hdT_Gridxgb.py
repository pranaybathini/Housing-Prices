import pandas as pd
import numpy as np
import csv
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import datetime

    
with open('actual_train.csv') as csvfile:
	data = pd.read_csv(csvfile,delimiter=',')
	
	
	
	
	data['Builder Name'].fillna(np.nan,inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['Builder Name'].values))
	data['Builder Name'] = lbl.transform(list(data['Builder Name'].values))

	
	for x in data['Date Built']:
		df = datetime.datetime.strptime(x, "%m/%d/%Y %I:%M %p").strftime("%m/%d/%Y %H:%M")
		data['Date Built'].replace(x,df)
	data['Date Built'] = pd.to_datetime(data['Date Built'])
	data['Date Built'] = (data['Date Built'] - data['Date Built'].min())  / np.timedelta64(1,'D')
	
	for xyy in data['Date Priced']:
		df = datetime.datetime.strptime(xyy, "%m/%d/%Y %I:%M %p").strftime("%m/%d/%Y %H:%M")
		data['Date Priced'].replace(xyy,df)
	data['Date Priced'] = pd.to_datetime(data['Date Priced'])
	data['Date Priced'] = (data['Date Priced'] - data['Date Priced'].min())  / np.timedelta64(1,'D')
	

	data['garden'].fillna(np.nan,inplace=True)
	#data['garden'] = pd.DataFrame(data['garden'])
	#data['garden'].fillna(0).rolling(window=2,min_periods=1).max()
	

	data['Dock'].fillna(np.nan,inplace=True)
	data['Capital'].fillna(np.nan,inplace=True)
	data['Royal Market'].fillna(np.nan,inplace=True)
	data['Guarding Tower'].fillna(np.nan,inplace=True)
	data['River'].fillna(np.nan,inplace=True)
	
	data['renovation'].fillna(np.nan,inplace=True)
	#data['renovation'] = pd.DataFrame(data['renovation'])
	#data['renovation'].fillna(0).rolling(window=2,min_periods=1).max()
	
	
	data['dining rooms'].fillna(np.nan,inplace=True)
	data['bedrooms'].fillna(np.nan,inplace=True)
	data['bathrooms'].fillna(np.nan,inplace=True)
	
	data['visit'].fillna(np.nan,inplace=True)
	#data['visit'] = pd.DataFrame(data['visit'])
	#data['visit'].fillna(0).rolling(window=2,min_periods=1).max()
	

	data['Sorcerer'].fillna(np.nan,inplace=True)
	#data['Sorcerer'] = pd.DataFrame(data['Sorcerer'])
	#data['Sorcerer'].fillna(0).rolling(window=2,min_periods=1).max()
	
	data['blessings'].fillna(np.nan,inplace=True)
	
	data['land'].fillna(np.nan,inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['land'].values))
	data['land'] = lbl.transform(list(data['land'].values))
	
	data['Location'].fillna(np.nan,inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['Location'].values))
	data['Location'] = lbl.transform(list(data['Location'].values))
	
	
	data['Holy tree'].fillna(np.nan,inplace=True)
	#data['Holy tree'] = pd.DataFrame(data['Holy tree'])
	#data['Holy tree'].fillna(0).rolling(window=2,min_periods=1).max()
	
	data['Knight\'s house'].fillna(np.nan,inplace=True)
	y = data['Golden Grains']
	del data['Golden Grains']
	del data['House ID'] 
	X = data
	
	with open('test.csv') as TestData:
		data1 = pd.read_csv(TestData,delimiter=',')
		
		data1['Builder Name'].fillna(np.nan,inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['Builder Name'].values))
		data1['Builder Name'] = lbl.transform(list(data1['Builder Name'].values))

	
		for x in data1['Date Built']:
			df = datetime.datetime.strptime(x, "%m/%d/%Y %I:%M %p").strftime("%m/%d/%Y %H:%M")
			data1['Date Built'].replace(x,df)
		data1['Date Built'] = pd.to_datetime(data1['Date Built'])
		data1['Date Built'] = (data1['Date Built'] - data1['Date Built'].min())  / np.timedelta64(1,'D')
		
		for xyy in data1['Date Priced']:
			df = datetime.datetime.strptime(xyy, "%m/%d/%Y %I:%M %p").strftime("%m/%d/%Y %H:%M")
			data1['Date Priced'].replace(xyy,df)
		data1['Date Priced'] = pd.to_datetime(data1['Date Priced'])
		data1['Date Priced'] = (data1['Date Priced'] - data1['Date Priced'].min())  / np.timedelta64(1,'D')
		
		
		
		data1['garden'].fillna(np.nan,inplace=True)
		#data1['garden'] = pd.DataFrame(data1['garden'])
		#data1['garden'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['Dock'].fillna(np.nan,inplace=True)
		data1['Capital'].fillna(np.nan,inplace=True)
		data1['Royal Market'].fillna(np.nan,inplace=True)
		data1['Guarding Tower'].fillna(np.nan,inplace=True)
		data1['River'].fillna(np.nan,inplace=True)
		
		data1['renovation'].fillna(np.nan,inplace=True)
		#data1['renovation'] = pd.DataFrame(data1['renovation'])
		#data1['renovation'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['dining rooms'].fillna(np.nan,inplace=True)
		data1['bedrooms'].fillna(np.nan,inplace=True)
		data1['bathrooms'].fillna(np.nan,inplace=True)
		
		data1['visit'].fillna(np.nan,inplace=True)
		#data1['visit'] = pd.DataFrame(data1['visit'])
		#data1['visit'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['Sorcerer'].fillna(np.nan,inplace=True)
		#data1['Sorcerer'] = pd.DataFrame(data1['Sorcerer'])
		#data1['Sorcerer'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['blessings'].fillna(np.nan,inplace=True)
		
		data1['land'].fillna(np.nan,inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['land'].values))
		data1['land'] = lbl.transform(list(data1['land'].values))

		data1['Location'].fillna(np.nan,inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['Location'].values))
		data1['Location'] = lbl.transform(list(data1['Location'].values))
		
		data1['Holy tree'].fillna(np.nan,inplace=True)
		#data1['Holy tree'] = pd.DataFrame(data1['Holy tree'])
		#data1['Holy tree'].fillna(0).rolling(window=2,min_periods=1).max()
		data1['Knight\'s house'].fillna(np.nan,inplace=True)
		yx = data1['House ID']
		del data1['House ID'] 
		
		import xgboost as xgb
		from sklearn.grid_search import GridSearchCV
		cv_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
		ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'seed':0, 'subsample': 0.8, 'colsample_bytree': 0.8, 'objective': 'binary:logistic'}
		optimized_GBM = GridSearchCV(xgb.XGBClassifier(**ind_params), cv_params, scoring = 'accuracy', cv = 5, n_jobs = 3)
		optimized_GBM.fit(X,y)
		prediction1=optimized_GBM.predict(data1)
		with open('result.csv',"w") as f:
			writer = csv.writer(f)
			ps = ['House ID','Golden Grains']
			writer.writerow(ps)
			
			for x,vc  in  zip(yx,prediction1):
				writer.writerow([x,vc])
					
			
	
	
	
