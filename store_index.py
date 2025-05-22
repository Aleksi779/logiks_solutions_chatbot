from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load Api Key
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY



# Extract data from pdf
extracted_data = load_pdf_file(data='Data/')

# Create text chunks from data of the pdf
text_chunks = text_split(extracted_data)

# Download the embedding model from HuggingFace
embeddings = download_hugging_face_embeddings()



# Create Pinecone database
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "companychatbot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)


# Embed each chunk (create vectors from each chunk) and save the embeddings into Pinecone database
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)