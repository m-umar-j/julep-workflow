from fastapi import FastAPI, File
from pydantic_models import NmapRequest, NmapResponse, SqlmapRequest, SqlmapResponse
import logging
import requests
import subprocess

logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

@app.post("/nmap-scan", response_model=NmapResponse) 
def nmap_scan(domain: NmapRequest):
    target = domain.target
    if not target: 
        raise HTTPException(status_code=400, detail="No target provided")
    try:
        result = subprocess.run(['nmap', target], capture_output=True, text=True, timeout=60)
        return NmapResponse(output=result.stdout)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sqlmap-scan", response_model=SqlmapResponse)
def sqlmap_scan(request: SqlmapRequest):
    url = request.url
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided")
    try:
        result = subprocess.run(['sqlmap', '-u', url, '--batch'], capture_output=True, text=True, timeout=120)
        return SqlmapResponse(output=result.stdout)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("ffuf-scan", response_model=FfufResponse)
def ffuf_scan(request: FfufRequest):
    url = request.url
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided")
    try:
        result = subprocess.run(['ffuf', '-u', url, '--batch'], capture_output=True, text=True, timeout=120) # I may have to change the command
        return SqlmapResponse(output=result.stdout)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



    
