# Lexicon Ai - Chat with your documents

## 🧠 HackRx LLM Document Processing API

A powerful FastAPI-based system by **Team CommitSquad** (Siddharth & Akul) that uses **Google Gemini** to answer natural language queries from **uploaded documents** like policies, legal contracts, HR manuals, and more.

**Try the AI**: [https://lexicon-ai-eight.vercel.app/](https://lexicon-ai-eight.vercel.app/)

🔗 **Live API**: [https://hackrx-llm-api-sj2g.onrender.com](https://hackrx-llm-api-sj2g.onrender.com/docs)

👉 **Query (send request here):** [https://hackrx-llm-api-sj2g.onrender.com/api/query](https://hackrx-llm-api-sj2g.onrender.com/api/query)

---

## ✨ Features

- 📁 Upload **multiple documents** (PDF, DOCX, MSG/email)
- ❓ Ask **multiple natural language questions**
- 🤖 Powered by **Gemini 1.5 Flash LLM + Embeddings**
- 🔍 Retrieves document clauses via **FAISS** semantic search
- 📊 Returns structured **JSON answers with clause references**
- ⚡ Built with **FastAPI**, hosted on **Render (Free Tier)**

---

## 🚀 How It Works

1. **Upload Files** — one or more documents  
2. **Ask Questions** — natural language queries  
3. **Receive Answers** — decision + justification + source chunk(s)

---

## 🛠 Tech Stack

| Component      | Tech                          |
|----------------|-------------------------------|
| LLM            | Gemini 2.5 Flash              |
| Embeddings     | gemini-embedding-001          |
| API Backend    | FastAPI                       |
| Vector DB      | FAISS                         |
| Hosting        | Render                        |
| Input Formats  | PDF, DOCX, MSG                |

---

## 📦 API Usage

### POST `/query/`

| Field      | Type             | Description                  |
|------------|------------------|------------------------------|
| `files`    | List[UploadFile] | One or more documents        |
| `questions`| List[str]        | One or more queries          |

📄 Try it live at: [`/docs`](https://hackrx-llm-api-sj2g.onrender.com/docs)

---

## ✅ Example Response

```json
{
  "results": [
    {
      "question": "Is knee surgery covered?",
      "top_chunks": [
        "Clause 4.2: Knee surgery is covered after 90 days.",
        "Surgeries due to accidents are covered from day one."
      ],
      "response": {
        "decision": "Approved",
        "amount_or_value": "Not specified",
        "justification": "As per Clause 4.2, knee surgery is covered after 90 days."
      }
    }
  ]
}
```
## Create Environment
```bash
# Create venv (for all os)
python3 -m venv venv

# Activate (for macOS)
source venv/bin/activate

# Activate (for Windows)
venv\Scripts\Activate.ps1
```

---

## 🧪 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Add your Gemini key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run locally
uvicorn server.main:app --reload
```
### Add your gemini api key in .env, and enjoy 😌.
---

## 👨‍💻 Team: CommitSquad

- **Siddharth** – Full-stack dev, LLM orchestration, API logic, document handling & embeddings
- **Akul** – Database engineer (Mysql), Database deployment

---

## 🤝 Acknowledgements

Built with ❤️ for **HackRx 6.0**  
Powered by **Google Gemini**, **FAISS**, and **Render**

---

## 📬 Contact

Drop us a message if you'd like to collaborate or test our system!
