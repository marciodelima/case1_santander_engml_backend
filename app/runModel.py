import sys
import numpy as np
import pandas as pd
import pickle
import os
import glob
import sklearn

def run(dt): 
	
	#Inserindo valores FAKE devido ao one hot encoder / Dummies
	new_row = {"age": 40, "sex": 0, "chest_pain_type": 1, "resting_blood_pressure": 145, "cholesterol": 233, "fasting_blood_sugar": 0, "rest_ecg": 0, "max_heart_rate_achieved": 150, "exercise_induced_angina": 0, "st_depression": 2.3, "st_slope": 1, "num_major_vessels": 0, "thalassemia": 0}
	dt = dt.append(new_row, ignore_index=True)
	new_row = {"age": 40, "sex": 1, "chest_pain_type": 2, "resting_blood_pressure": 145, "cholesterol": 233, "fasting_blood_sugar": 1, "rest_ecg": 1, "max_heart_rate_achieved": 150, "exercise_induced_angina": 1, "st_depression": 2.3, "st_slope": 2, "num_major_vessels": 1, "thalassemia": 1}
	dt = dt.append(new_row, ignore_index=True)
	new_row = {"age": 40, "sex": 1, "chest_pain_type": 3, "resting_blood_pressure": 145, "cholesterol": 233, "fasting_blood_sugar": 1, "rest_ecg": 2, "max_heart_rate_achieved": 150, "exercise_induced_angina": 1, "st_depression": 2.3, "st_slope": 3, "num_major_vessels": 2, "thalassemia": 2}
	dt = dt.append(new_row, ignore_index=True)
	new_row = {"age": 40, "sex": 1, "chest_pain_type": 4, "resting_blood_pressure": 145, "cholesterol": 233, "fasting_blood_sugar": 1, "rest_ecg": 2, "max_heart_rate_achieved": 150, "exercise_induced_angina": 1, "st_depression": 2.3, "st_slope": 3, "num_major_vessels": 3, "thalassemia": 3}
	dt = dt.append(new_row, ignore_index=True)

	#Transformações dos dados	
	dt['sex'][dt['sex'] == 0] = 'female'
	dt['sex'][dt['sex'] == 1] = 'male'

	dt['chest_pain_type'][dt['chest_pain_type'] == 1] = 'typical angina'
	dt['chest_pain_type'][dt['chest_pain_type'] == 2] = 'atypical angina'
	dt['chest_pain_type'][dt['chest_pain_type'] == 3] = 'non-anginal pain'
	dt['chest_pain_type'][dt['chest_pain_type'] == 4] = 'asymptomatic'

	dt['fasting_blood_sugar'][dt['fasting_blood_sugar'] == 0] = 'lower than 120mg/ml'
	dt['fasting_blood_sugar'][dt['fasting_blood_sugar'] == 1] = 'greater than 120mg/ml'

	dt['rest_ecg'][dt['rest_ecg'] == 0] = 'normal'
	dt['rest_ecg'][dt['rest_ecg'] == 1] = 'ST-T wave abnormality'
	dt['rest_ecg'][dt['rest_ecg'] == 2] = 'left ventricular hypertrophy'

	dt['exercise_induced_angina'][dt['exercise_induced_angina'] == 0] = 'no'
	dt['exercise_induced_angina'][dt['exercise_induced_angina'] == 1] = 'yes'

	dt['st_slope'][dt['st_slope'] == 1] = 'upsloping'
	dt['st_slope'][dt['st_slope'] == 2] = 'flat'
	dt['st_slope'][dt['st_slope'] == 3] = 'downsloping'

	dt['thalassemia'][dt['thalassemia'] == 1] = 'normal'
	dt['thalassemia'][dt['thalassemia'] == 2] = 'fixed defect'
	dt['thalassemia'][dt['thalassemia'] == 3] = 'reversable defect'

	dt['sex'] = dt['sex'].astype('object')
	dt['chest_pain_type'] = dt['chest_pain_type'].astype('object')
	dt['fasting_blood_sugar'] = dt['fasting_blood_sugar'].astype('object')
	dt['rest_ecg'] = dt['rest_ecg'].astype('object')
	dt['exercise_induced_angina'] = dt['exercise_induced_angina'].astype('object')
	dt['st_slope'] = dt['st_slope'].astype('object')
	dt['thalassemia'] = dt['thalassemia'].astype('object')	
	
	dt = pd.get_dummies(dt, drop_first=True)

	#Carregando o modelo - Versão mais recente
	diretorio = os.path.abspath(__file__ + "/../../modelo/")
	files_path = os.path.join(diretorio, '*.pkl')
	files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True) 
	model=pickle.load(open(files[0],'rb'))	
	
	y_predict = model.predict(dt)
	y_pred_quant = model.predict_proba(dt)
	
	dt_saida = pd.DataFrame(columns=['resultado', 'probabilidade'])
	new_row = {"resultado": y_predict[0], "probabilidade": y_pred_quant[0][y_predict[0]]}
	dt_saida = dt_saida.append(new_row, ignore_index=True)

	print(dt_saida)

	return dt_saida
