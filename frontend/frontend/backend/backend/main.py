from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_attendance

app = FastAPI()

class Attendance(BaseModel):
    name: str
    attendance: float

@app.post("/predict")
def predict(data: Attendance):
    result = predict_attendance(data.attendance)
    return {
        "student": data.name,
        "result": result
    }
