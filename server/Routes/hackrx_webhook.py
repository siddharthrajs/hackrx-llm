from fastapi import APIRouter, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import requests
import os
import traceback

from server.file_processor import extract_text
from server.chunker import chunk_text
from server.embedding_utils import embed_texts
from server.faiss_utils import create_faiss_index, search_similar_chunks
from server.answer_generator import get_structured_answer

router = APIRouter()

TEAM_TOKEN = "003f72107f3a86b7513ea5bb6b348b9e813b2c45e2b19429180455cffc0c3755"

class HackRxRequest(BaseModel):
    documents: str
    questions: List[str]

@router.post("/api/v1/hackrx/run", summary="HackRx Webhook")
async def hackrx_webhook(
    payload: HackRxRequest,
    authorization: str = Header(None)
):
    try:
        # Step 0: Auth check
        if authorization != f"Bearer {TEAM_TOKEN}":
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Step 1: Download the document
        response = requests.get(payload.documents)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Document download failed")

        file_path = "temp_webhook.pdf"
        with open(file_path, "wb") as f:
            f.write(response.content)

        # Step 2: Extract text
        raw_text = extract_text(file_path)
        os.remove(file_path)

        # Step 3: Chunk, embed, index
        chunks = chunk_text(raw_text)
        embeddings = embed_texts(chunks)
        index = create_faiss_index(embeddings)

        # Step 4: Query each question
        answers = []
        for question in payload.questions:
            q_embedding = embed_texts([question])[0]
            top_chunks = search_similar_chunks(q_embedding, index, chunks, k=3)
            result = get_structured_answer(question, top_chunks)

            # Just extract plain string answer
            if isinstance(result, dict) and "justification" in result:
                answers.append(result["justification"])
            elif isinstance(result, dict) and "decision" in result:
                answers.append(result["decision"])
            else:
                answers.append(str(result))

        return JSONResponse(content={"answers": answers})

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
