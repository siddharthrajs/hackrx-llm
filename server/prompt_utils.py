def build_prompt(query, relevant_chunks):
    chunks_text = "\n\n".join(relevant_chunks)

    return f"""
You are an expert AI assistant that helps interpret and extract insights from documents of various domains — such as insurance policies, legal agreements, HR manuals, technical specs, compliance docs, etc.

Below are excerpts retrieved from one or more documents:

------------------ DOCUMENT EXCERPTS ------------------

{chunks_text}

-------------------------------------------------------

User Question:
"{query}"

Your task is to:
- Analyze the question
- Refer ONLY to the given document excerpts
- Make an informed decision based on the logic or rules present
- Provide a justification that clearly maps to specific clause(s) or section(s)
- Include any relevant amount, deadline, or condition mentioned

You must return your response in this exact structured JSON format:

{{
  "decision": "<Approved/Rejected/Yes/No/Found/Not Found/etc. — one phrase summary>",
  "amount_or_value": "<If applicable, else 'None'>",
  "justification": "<Short explanation with reference to exact phrases or clauses>"
}}

**Output ONLY the JSON. Do NOT include any additional explanation or text.**
"""
