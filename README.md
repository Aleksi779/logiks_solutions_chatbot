# logiks_solutions_chatbot


# How to run?
### Steps:


Clone the repository


```bash 
Project repo: https://github.com
```

### Step 01 - Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.13 -y
```

```bash
conda activate llmapp
```

### Step 02 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 03 - Create a .env file in the root directory and add your Pinecone & openai api keys as follows:

```ini
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Run following command to store embeddings to pinecone
python store_index.py
```

```bash
# Run the following command to start the application
python app.py
```

Now,
```bash
open up localhost:
```

### Tech stack used:

- Python
- Langchain
- Flask
- GPT
- Pinecone