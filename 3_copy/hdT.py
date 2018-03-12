
import pandas as pd
import numpy as np
import csv
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

    
with open('actual_train.csv') as csvfile:
	data = pd.read_csv(csvfile,delimiter=',')
	
	data['Builder Name'].fillna('Nan',inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['Builder Name'].values))
	data['Builder Name'] = lbl.transform(list(data['Builder Name'].values))

	data['garden'].fillna(0,inplace=True)
	data['garden'] = pd.DataFrame(data['garden'])
	data['garden'].fillna(0).rolling(window=2,min_periods=1).max()
	

	data['Dock'].fillna(data['Dock'].mean(),inplace=True)
	data['Capital'].fillna(data['Capital'].mean(),inplace=True)
	data['Royal Market'].fillna(data['Royal Market'].mean(),inplace=True)
	data['Guarding Tower'].fillna(data['Guarding Tower'].mean(),inplace=True)
	data['River'].fillna(data['River'].mean(),inplace=True)
	
	data['renovation'].fillna(0,inplace=True)
	data['renovation'] = pd.DataFrame(data['renovation'])
	data['renovation'].fillna(0).rolling(window=2,min_periods=1).max()
	
	
	data['dining rooms'].fillna(data['dining rooms'].mean(),inplace=True)
	data['bedrooms'].fillna(data['bedrooms'].mean(),inplace=True)
	data['bathrooms'].fillna(data['bathrooms'].mean(),inplace=True)
	
	data['visit'].fillna(0,inplace=True)
	data['visit'] = pd.DataFrame(data['visit'])
	data['visit'].fillna(0).rolling(window=2,min_periods=1).max()
	

	data['Sorcerer'].fillna(0,inplace=True)
	data['Sorcerer'] = pd.DataFrame(data['Sorcerer'])
	data['Sorcerer'].fillna(0).rolling(window=2,min_periods=1).max()
	
	data['blessings'].fillna(data['blessings'].mean(),inplace=True)
	
	data['land'].fillna(0,inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['land'].values))
	data['land'] = lbl.transform(list(data['land'].values))
	
	data['Location'].fillna(0,inplace=True)
	lbl = preprocessing.LabelEncoder()
	lbl.fit(list(data['Location'].values))
	data['Location'] = lbl.transform(list(data['Location'].values))
	
	data['Holy tree'].fillna(0,inplace=True)
	data['Holy tree'] = pd.DataFrame(data['Holy tree'])
	data['Holy tree'].fillna(0).rolling(window=2,min_periods=1).max()
	
	data['Knight\'s house'].fillna(data['Knight\'s house'].mean(),inplace=True)
	y = data['Golden Grains']
	del data['Golden Grains']
	del data['House ID'] 
	del data['Date Built']
	del data['Date Priced']
	X = data
	
	with open('test.csv') as TestData:
		data1 = pd.read_csv(TestData,delimiter=',')
		
		data1['Builder Name'].fillna('Nan',inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['Builder Name'].values))
		data1['Builder Name'] = lbl.transform(list(data1['Builder Name'].values))
		
		data1['garden'].fillna(0,inplace=True)
		data1['garden'] = pd.DataFrame(data1['garden'])
		data1['garden'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['Dock'].fillna(data1['Dock'].mean(),inplace=True)
		data1['Capital'].fillna(data1['Capital'].mean(),inplace=True)
		data1['Royal Market'].fillna(data1['Royal Market'].mean(),inplace=True)
		data1['Guarding Tower'].fillna(data1['Guarding Tower'].mean(),inplace=True)
		data1['River'].fillna(data1['River'].mean(),inplace=True)
		
		data1['renovation'].fillna(0,inplace=True)
		data1['renovation'] = pd.DataFrame(data1['renovation'])
		data1['renovation'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['dining rooms'].fillna(data1['dining rooms'].mean(),inplace=True)
		data1['bedrooms'].fillna(data1['bedrooms'].mean(),inplace=True)
		data1['bathrooms'].fillna(data1['bathrooms'].mean(),inplace=True)
		
		data1['visit'].fillna(0,inplace=True)
		data1['visit'] = pd.DataFrame(data1['visit'])
		data1['visit'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['Sorcerer'].fillna(0,inplace=True)
		data1['Sorcerer'] = pd.DataFrame(data1['Sorcerer'])
		data1['Sorcerer'].fillna(0).rolling(window=2,min_periods=1).max()
		
		data1['blessings'].fillna(data1['blessings'].mean(),inplace=True)
		
		data1['land'].fillna(0,inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['land'].values))
		data1['land'] = lbl.transform(list(data1['land'].values))
	
		data1['Location'].fillna(0,inplace=True)
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(data1['Location'].values))
		data1['Location'] = lbl.transform(list(data1['Location'].values))
	
		data1['Holy tree'].fillna(0,inplace=True)
		data1['Holy tree'] = pd.DataFrame(data1['Holy tree'])
		data1['Holy tree'].fillna(0).rolling(window=2,min_periods=1).max()
		data1['Knight\'s house'].fillna(data1['Knight\'s house'].mean(),inplace=True)
		yx = data1['House ID']
		del data1['House ID'] 
		del data1['Date Built']
		del data1['Date Priced']
	
		#import xgboost as xgb
		#from sklearn.grid_search import GridSearchCV
		#cv_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
		#ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'seed':0, 'subsample': 0.8, 'colsample_bytree': 0.8,'objective': 'binary:logistic'}
		#optimized_GBM = GridSearchCV(xgb.XGBClassifier(**ind_params),cv_params, scoring = 'accuracy', cv = 5, n_jobs = -1)

		#optimized_GBM.fit((X ,y)
		#print(optimized_GBM.grid_scores)
		#sns.set()
		#xgb.plot_importance(final_gb)
		#importances = final_gb.get_fscore()
		#print(importances)
		#prediction1 = optimized_GBM.predict(data1)
		from xgboost.sklearn import XGBRegressor
		reg5 = XGBRegressor(max_depth=8,min_child_weight=1,n_estimators=301,learning_rate=0.1)
		reg5.fit(X ,y)
		prediction1 = reg5.predict(data1)
		
		with open('result.csv',"w") as f:
			writer = csv.writer(f)
			ps = ['House ID','Golden Grains']
			writer.writerow(ps)
			
			for x,vc  in  zip(yx,prediction1):
				writer.writerow([x,vc])
					
			
	
	
	
