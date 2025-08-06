from fastapi import APIRouter
import os
from fastapi import UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List, Annotated
import traceback

from server.file_processor import extract_text
from server.chunker import chunk_text
from server.embedding_utils import embed_texts
from server.faiss_utils import create_faiss_index, search_similar_chunks
from server.answer_generator import get_structured_answer

router = APIRouter()

@router.post("/query/", summary="Query multiple questions across uploaded documents")
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
            if not extracted:
                extracted = " "
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