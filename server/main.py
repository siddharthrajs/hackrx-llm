from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.Routes.post_ques import router as post_ques_router
from server.Routes.hackrx_webhook import router as hackrx_router



app = FastAPI(
    title="LLM Document Reasoning API",
    description="Upload multiple documents and ask multiple questions. Get structured answers from Gemini.",
    version="2.0.0",
)

# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_ques_router, prefix="/api", tags=["Document Query"])

app.include_router(hackrx_router)

@app.get("/", summary="Health Check")
async def health_check():
    return {"status": "ok", "message": "LLM Document Reasoning API is running!"}