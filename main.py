from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Initialize FastAPI
app = FastAPI()

# Load trained model and encoders
final_model = joblib.load("teacher_burnout_model.pkl")
encoders = joblib.load("label_encoders.pkl")
trained_features = joblib.load("trained_feature_order.pkl")

# Define categorical columns
categorical_cols = ["Country", "EmploymentType", "Occupation", "WorkFromHome", "PartnershipStatus"]

# Define Input Schema
class InputData(BaseModel):
    Country: str
    EmploymentType: str
    Occupation: str
    WorkFromHome: str
    HardConcentrateWork: int
    lonely3: int
    FeelingRejected: int
    SubjectiveIncome: int
    Happiness: int
    PartnershipStatus: str



@app.post("/predict")
def predict(data: InputData):
    print(f"Received Data: {data}")  # Debugging Step ✅
    return {"message": "Data received successfully"}
    test_input = pd.DataFrame([data.dict()])

    # Convert categorical columns to string
    for col in categorical_cols:
        test_input[col] = test_input[col].astype(str)

        # Handle unseen categorical values
        common_category = encoders[col].classes_[0]  
        test_input[col] = test_input[col].map(
            lambda x: encoders[col].classes_.tolist().index(x) if x in encoders[col].classes_ else encoders[col].classes_.tolist().index(common_category)
        )

    # Ensure column order matches training data
    test_input = test_input.reindex(columns=trained_features, fill_value=0)

    # Make prediction
    prediction = final_model.predict(test_input)[0]

    return {"burnout_risk": int(prediction)}
