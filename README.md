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

