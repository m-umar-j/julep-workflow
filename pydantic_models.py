from pydantic import BaseModel

class NmapRequest(BaseModel):
    target: str

class NmapResponse(BaseModel):
    output: str

class SqlmapRequest(BaseModel):
    url: str

class SqlmapResponse(BaseModel):
    output: str

