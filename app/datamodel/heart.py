from pydantic import BaseModel, Field

class Heart(BaseModel): 
	age: int
	sex: int
	chest_pain_type: int
	resting_blood_pressure: int
	cholesterol: int
	fasting_blood_sugar: int
	rest_ecg: int
	max_heart_rate_achieved: int
	exercise_induced_angina: int
	st_depression: float
	st_slope: int
	num_major_vessels: int
	thalassemia: int
