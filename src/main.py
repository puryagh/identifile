import src.api.version
import src.api.identify
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/version")
def version():
    return src.api.version.version()


@app.post("/identify")
def identify(file: UploadFile = File(...)):
    return src.api.identify.identify(file)


@app.post("/ai_identify")
def ai_identify(file: UploadFile = File(...)):
    return src.api.identify.ai_identify(file)
