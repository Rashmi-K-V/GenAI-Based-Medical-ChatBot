# 🧠 GenAI-Based Medical ChatBot

A Generative AI-powered Medical ChatBot built using the Gale Encyclopedia of Medicine as its knowledge base. This chatbot can intelligently answer medical queries by extracting and processing content from a trusted PDF source using LLMs like **Gemini** and **LangChain**. Vector search is powered by **Pinecone**, and the app is served with **Flask**.

---

## 🚀 Features

- 📚 **Gale Encyclopedia of Medicine Integration**  
  Extracts and chunks data from a PDF medical encyclopedia to serve as the knowledge base.

- 🔎 **Contextual Semantic Search**  
  Uses vector similarity search (via Pinecone) to find the most relevant context chunks for each query.

- 💬 **LLM-Powered Response Generation**  
  Generates high-quality medical answers using Gemini or other LLMs integrated via LangChain.

- 🌐 **Web Interface (Flask)**  
  A simple and user-friendly web interface to interact with the chatbot.

- 🧠 **LangChain Support**  
  Easily extensible using LangChain’s modular architecture.

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Pinecone](https://www.pinecone.io/)
- [PyMuPDF / PyPDFLoader](https://pypi.org/project/pymupdf/)
- [Jupyter Notebook](https://jupyter.org/) (for development and testing)

## Technologies Used

- **Flask**: Lightweight web framework for building the backend of the chatbot.
- **LangChain**: A framework for building applications that use large language models (LLMs).
- **Pinecone**: Vector database for storing and querying medical knowledge embeddings.
- **Gemini**: A large language model for natural language understanding and generation.
- **Python**: The primary programming language used.

## Features

- **Conversational Medical Assistance**: The chatbot can answer various medical-related questions based on its training data and external knowledge sources.
- **Contextual Conversations**: The chatbot can retain context across interactions to provide more accurate answers.
- **Knowledge Search**: Uses Pinecone to search through indexed medical knowledge for relevant information.

## Setup and Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A virtual environment (recommended)

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Rashmi-K-V/GenAI-Based-Medical-ChatBot.git
   cd GenAI-Based-Medical-ChatBot
   ```

2. **Create and activate a virtual environment**:

   For **Windows**:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   For **macOS/Linux**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   For gemini model:

   ```bash
   pip install langchain-google-genai==0.0.6 google-generativeai==0.3.2
   ```

4. **Run the application**:

   To start the Flask app locally, run:

   ```bash
   flask run
   ```

   The app should now be running at `http://127.0.0.1:5000`.

## Usage

Once the application is running, you can interact with the chatbot by navigating to the provided URL and typing in medical-related queries. The bot will use the underlying models to respond based on its training data and indexed knowledge.

### Example Conversation

1. **User**: "What are the symptoms of diabetes?"
2. **Bot**: "Diabetes symptoms include increased thirst, frequent urination, extreme fatigue, and blurred vision."

### Steps for contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
