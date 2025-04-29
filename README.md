# Experiment

1. Front end test
   cd frontend
   npm run dev

2. Back end test
   cd backend
   uvicorn app.main:app --reload

The backend should now be running at http://localhost:8000

You can test if it's working by:
Opening http://localhost:8000 in your browser (should see "AI Agent API is running" message)

Make sure you've replaced the placeholder API keys in backend/.env with your actual:
OpenAI API key
Pinecone API key
Pinecone environment



# AI Agent Project

A full-stack AI agent using Next.js frontend and FastAPI backend.

## Setup

### Backend
1. Create and activate virtual environment:


python
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

2. Install dependencies:

bash
npm install
npm install axios @types/axios

2. Run the development server:

bash:README.md
npm run dev


## Environment Variables
Backend:
- OPENAI_API_KEY
- PINECONE_API_KEY
- PINECONE_ENVIRONMENT

Frontend:
- NEXT_PUBLIC_API_URL=http://localhost:8000
