import joblib
import pandas as pd

model = joblib.load("model.pkl")

def detect(response_time):
    df = pd.DataFrame([[response_time]], columns=["response_time"])
    prediction = model.predict(df)
    return prediction[0] == -1

