import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.inference import Chatbot_Response
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):

    message: str


@app.post("/chat")

def chatbot_endpoint(request: ChatRequest):

    response = Chatbot_Response(request.message)

    return {"response":response}

