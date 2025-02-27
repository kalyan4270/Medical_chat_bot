from src.helper import load_pdf, text_split, download_google_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY =  os.environ.get("PINECONE_API_KEY")

extracted_data = load_pdf(data="Data/")
text_chunks = text_split(extracted_data)
embeddings = download_google_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "cricbot"

pc.create_index(
    name=index_name,
    dimension=768, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

docsearch = PineconeVectorStore.from_documents(documents=text_chunks,
                                               index_name = index_name, 
                                               embedding=embeddings)

