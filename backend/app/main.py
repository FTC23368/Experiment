from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI and Pinecone
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

@app.get("/")
async def read_root():
    return {"message": "AI Agent API is running"}

@app.post("/chat")
async def chat(message: str):
    response = llm.predict(message)
    return {"response": response} 