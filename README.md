# Lexicon Ai - Chat with your documents

## 🧠 HackRx LLM Document Processing API

A powerful FastAPI-based system by **Team CommitSquad** (Siddharth & Akul) that uses **Google Gemini** to answer natural language queries from **uploaded documents** like policies, legal contracts, HR manuals, and more.

**Try the AI**: [https://lexicon-ai-eight.vercel.app/](https://lexicon-ai-eight.vercel.app/)

🔗 **Live API**: [http://b4cocwc8okkw44go8kc8c0gk.129.159.230.243.sslip.io/](http://b4cocwc8okkw44go8kc8c0gk.129.159.230.243.sslip.io/)

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

## 🐳 Docker Setup (Recommended)

### Quick Start with Docker

```bash
# 1. Add your Gemini API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 2. Run the application
./run.sh

# Or manually:
# docker-compose build
# docker-compose up -d
```

### Docker Commands

```bash
# Build the image
docker-compose build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down

# Rebuild after code changes
docker-compose up --build
```

---

## 🧪 Local Development (Alternative)

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

## 🤝 Acknowledgements

Built with ❤️ for **HackRx 6.0**  
Powered by **Google Gemini**, **FAISS**, and **Render**

---

## 📬 Contact

Drop us a message if you'd like to collaborate or test our system!
