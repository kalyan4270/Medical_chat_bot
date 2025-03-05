# 🏏 CricBot - Your Cricket Chatbot

CricBot is an interactive chatbot designed to provide in-depth cricket knowledge. Whether you want to know much more about cricket, about the tournaments just like a cricket handbook, CricBot is here to assist!

## 🚀 Features
- 📢 **Instant Cricket Insights** – Ask about rules, teams, matches, and tournaments.
- 🎨 **Modern Chat UI** – Sleek, interactive, and user-friendly interface.
- ⚡ **Fast Responses** – Powered by an efficient backend.
- 📝 **Typing Indicator** – Provides a smooth conversational experience.
- 📜 **Auto-scrolling Chat Window** – Ensures a seamless chat experience.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kalyan4270/cricbot.git
cd cricbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Pinecone (Vector Database)

1. Create a Pinecone Account
2. Sign up at Pinecone
3. Get your API Key from the Pinecone console.

  
### 4️⃣ Create pinecone index

Run store-index file to create index in pinecone

``` bash
python store-index.py
```

### 5️⃣ Set Up Environment Variables

Create a .env file and add:

``` bash
PINECONE_API_KEY=your-api-key
GOOGLE_API_KEY= API-Key
```

### 6️⃣ Run the application

``` bash
python app.py
```

open http://127.0.0.1:8080/ in your browser


# 🖥️ Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: Pinecone (for retrieval-based responses)
- LangChain: Chaining retrieval and response generation
- Google Generative AI Embeddings: Embeddings for document storage

# 🏆 Future Improvements
 - Live Cricket Score Updates
 - Player & Team Analysis
 - Integration with Cricket APIs
