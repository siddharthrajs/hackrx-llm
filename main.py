from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Annotated
import os
import traceback

from file_processor import extract_text
from chunker import chunk_text
from embedding_utils import embed_texts
from faiss_utils import create_faiss_index, search_similar_chunks
from answer_generator import get_structured_answer

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

@app.post("/query/", summary="Query multiple questions across uploaded documents")
async def query_policy(
    files: Annotated[List[UploadFile], File(description="Upload PDF, DOCX, or email files")],
    questions: Annotated[List[str], Form(description="Add multiple natural language queries")]
):
    try:
        combined_text = ""

        # Step 1: Extract text from each uploaded file
        for file in files:
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as buffer:
                buffer.write(await file.read())

            extracted = extract_text(temp_path)
            combined_text += extracted + "\n\n"
            os.remove(temp_path)

        # Step 2: Chunk, embed, and build FAISS index
        chunks = chunk_text(combined_text)
        chunk_embeddings = embed_texts(chunks)
        index = create_faiss_index(chunk_embeddings)

        # Step 3: Process each query
        responses = []
        for query in questions:
            query_embedding = embed_texts([query])[0]
            top_chunks = search_similar_chunks(query_embedding, index, chunks, k=3)
            result = get_structured_answer(query, top_chunks)
            responses.append({
                "question": query,
                "top_chunks": top_chunks,
                "response": result
            })

        return JSONResponse(content={"results": responses})

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
