import os
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from utils import get_twitter_score, generate_proof, get_rank_proof

from pydantic import BaseModel

import uvicorn


app = FastAPI()

# middleware
app.add_middleware(
    CORSMiddleware, 
    allow_credentials=True, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

class score_respond(BaseModel):
    user_name : str

class proof_respond(BaseModel):
    rank : str

@app.post("/score_respond/")
async def score_respond(item: score_respond):
    features = get_twitter_score(item.user_name)
    print(features)
    respond = generate_proof(features)
    print(respond)
    return {"code":0, "data":respond}

@app.post("/proof_respond/")
async def proof_respond(item: proof_respond):
    proof = get_rank_proof(int(item.rank))
    print(proof)
    return {"code":0, "data":proof}

    

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)