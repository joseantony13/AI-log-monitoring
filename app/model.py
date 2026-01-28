import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = []

with open("app.log") as f:
    for line in f:
        response_time = int(line.split("Response time:")[1].replace("ms", ""))
        data.append(response_time)

df = pd.DataFrame(data, columns=["response_time"])

model = IsolationForest(contamination=0.1)
model.fit(df)

joblib.dump(model, "model.pkl")

