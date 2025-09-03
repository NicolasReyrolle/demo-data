import json

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

samples = json.load(open("datasets/sample.json", encoding="utf-8"))
luminosites = json.load(open("datasets/luminosite.json", encoding="utf-8"))

@app.get("/samples")
def read_samples():
    return samples

@app.get("/samples/{sample_id}")
def read_sample(sample_id: str):
    for sample in samples:
        if sample["id"] == sample_id:
            return sample

    raise HTTPException(status_code=404, detail="Sample not found")

@app.get("/luminosites")
def read_luminosites():
    return luminosites

@app.get("/luminosites/{luminosite_id}")
def read_luminosite(luminosite_id: int):
    for luminosite in luminosites:
        if luminosite["id"] == luminosite_id:
            return luminosite

    raise HTTPException(status_code=404, detail="Luminosite not found")
