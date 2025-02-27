from flask import Flask, render_template, jsonify, request
from src.helper import download_google_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY =  os.environ.get("PINECONE_API_KEY")

embeddings = download_google_embeddings()
index_name = "cricbot"

docsearch = PineconeVectorStore.from_existing_index(index_name = index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type = "similarity",search_kwargs={"k":3})
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", temperature= 0.5)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",System_prompt),
        ("human","{input}"),
    ]
)

question_ans_chain = create_stuff_documents_chain(llm,prompt)
rag_chain = create_retrieval_chain(retriever,question_ans_chain)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/get", methods = ["GET","POST"])

def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input" : msg})
    print("Response: ", response['answer'])
    return str(response['answer'])

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port= 8080,debug = True)
