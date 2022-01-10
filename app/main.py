import sys
import json
import pandas as pd
from app.datamodel.heart import Heart
from fastapi import FastAPI, Header, status
from fastapi.encoders import jsonable_encoder
from app.runModel import *

app = FastAPI(title="ML de Prevenção de doenças cardíacas", description="ML de Prevenção de doenças cardíacas", version="0.0.1")

@app.post("/preverDoencaCard", status_code=status.HTTP_201_CREATED, description="Prever doença cardíaca")
async def executarModelo(heart: Heart, content_type: str = Header(...)): 

	df = pd.DataFrame([heart.dict()])
	df_retorno = run(df)
	saida = df_retorno.to_json(orient="records", lines=True)
	return json.loads(saida)
