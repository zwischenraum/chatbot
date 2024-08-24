**LLM Streamlit Chat Interface with Ollama**
=====================================

A user-friendly Streamlit chat interface that utilizes the OpenAI API to converse with a locally-hosted Large Language Model (LLM) using Ollama. This interface provides a simple and intuitive way for users to interact with the LLM, allowing them to ask questions, engage in discussions, and explore its capabilities.

**Features**
------------

* **Text & Image Input:** Engage in conversations using both text and image prompts. 
* **Real-Time Responses:** See the LLM's responses generated in real time as it processes your input.
* **Image Display:** Uploaded images are seamlessly integrated into the conversation history.
* **Conversation Reset:**  Easily clear the chat history with a single button click to start fresh.

**Requirements**
---------------

* Python 3.x
* Poetry (for dependency management)
* Ollama and a running LLM (e.g., [llama-3.1-8b](https://ollama.com/library/llama3.1:8b))

**Installation**
--------------

To get started, run the following commands in your terminal:

```bash
poetry install
poetry shell
```

This will create a new virtual environment and install the required dependencies.

**Usage**
--------------

1. Run the application using `streamlit run main.py`.
2. Access the chat interface by navigating to `http://localhost:8501` in your web browser.
