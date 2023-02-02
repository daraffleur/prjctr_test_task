from pydantic import BaseModel


class TargetPredictionResponse(BaseModel):
    target: float
   