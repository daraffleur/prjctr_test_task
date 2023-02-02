import pandas as pd
from fastapi import APIRouter

from app.custom_types import TargetPredictionResponse
from app.models.ml import TargetPredictorModel
from app.utils import nlp_preprocessing


predict_router: APIRouter = APIRouter(tags=["Prediction"])


@predict_router.post("/predict", response_model=TargetPredictionResponse)
async def predict_target(text: str):
    model = TargetPredictorModel()
    df = pd.DataFrame({'excerpt': [text], 'prepared_text': [""]})
    df['prepared_text'][0] = nlp_preprocessing(df.excerpt[0])
    X_test = df.prepared_text
    test_tfidf = model.transform_train(X_test) 
    prediction = model.predict(test_tfidf)
    print("PPP", prediction)
    return {"target": prediction[0]}
