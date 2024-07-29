from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_index.llms.llama_api import LlamaAPI
import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = "API-KEY"

llm = LlamaAPI(api_key=api_key, max_tokens = 500)

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    prompt = f"You are a productivity coach. User said: '{message.text}'. Respond as a productivity coach in 100 words max."
    response = llm.complete(prompt)
    return {"response": response}

@app.get("/")
async def read_root():
    return {"message": "Server is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

