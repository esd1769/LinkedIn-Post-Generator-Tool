# 🤖 AI LinkedIn Post Generator

A **production-style Generative AI project** that goes beyond simple API usage by implementing a **complete AI content generation pipeline**.

Instead of directly prompting an LLM, this system uses **data preprocessing, retrieval, and structured prompting** to generate high-quality LinkedIn posts that closely match real-world writing styles. 🚀

---
**Note on Live Demo:** To maintain cost-efficiency and respect provider inactivity policies (e.g., Supabase's 90-day pause), the live deployment may occasionally be inactive. **Please refer to the Video Demo and the codebase for technical verification. I built this solo to master the fundamentals, but I've architected it using industry-standard naming conventions so that any senior engineer could step into this codebase and feel at home.**

## 🌟 Core Features

🧠 RAG-like preprocessing pipeline  
📚 Few-shot learning with real examples  
📝 Structured AI-generated LinkedIn posts  
🏷️ Intelligent tagging and metadata enrichment  
⚡ High-speed LLM inference  
🖥️ Interactive UI for real-time generation  
📊 Controlled and consistent output formatting  

---

## 🧰 Tech Stack

### 🧠 LLM & Inference
**Llama 3.2 (Open Source)** — Core language model  
**Groq Cloud** — High-speed inference for low latency responses  

### ⚙️ AI Pipeline
**Custom RAG-like Pipeline** — Preprocesses and structures data before generation  

### 🎯 Prompt Engineering
**Advanced Prompt Design** — Ensures structured JSON output, consistent tagging, and controlled formatting  

### 🖥️ Frontend / UI
**Streamlit** — Interactive web interface for real-time post generation  

### 🗄️ Data Handling
**JSON-based structured storage** — Stores enriched examples for retrieval  

---

## 💻 Local Setup Guide

Follow these steps to run the project locally:

### 1️⃣ Install Python
Download from  
https://www.python.org

### 2️⃣ Clone Repository
git clone REPOSITORY_URL  
cd project-folder  

### 3️⃣ Install Dependencies
pip install -r requirements.txt  

### 4️⃣ Run Application
streamlit run app.py  

Open your browser and visit  
http://localhost:8501  

---

## 🏗️ System Architecture

User --> StreamlitUI  
StreamlitUI --> InputHandler  
InputHandler --> RetrievalSystem  
RetrievalSystem --> JSONDataset  
RetrievalSystem --> FewShotExamples  
FewShotExamples --> PromptBuilder  
PromptBuilder --> LLM (Llama3.2 via Groq)  
LLM --> StructuredOutput  
StructuredOutput --> UI  

---

## 📈 Scaling & Production Notes

⚡ Groq enables ultra-fast LLM inference  
🧠 Few-shot learning improves output quality and consistency  
📚 Preprocessed dataset reduces runtime complexity  
🧩 Modular pipeline allows easy upgrades to models or prompts  

---

## 🎯 Who This Project Is For

👨‍💻 Developers learning Generative AI systems  
🧠 Engineers exploring RAG and LLM pipelines  
📚 Students building production-ready AI portfolios  
🚀 Anyone interested in AI-powered content generation  

---

## 📎 Useful Links

- [Groq](https://groq.com)  
- [Llama](https://ai.meta.com/llama/)  
- [Streamlit](https://streamlit.io)  
