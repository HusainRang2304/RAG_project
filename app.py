Python
```
import os
import glob
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA


# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# -------------------------
# Config
# -------------------------
DATA_PATH = "data"
DB_PATH = "vector_db"

st.set_page_config(page_title="RAG Knowledge Assistant", layout="wide")
st.title("📚 RAG-Based Knowledge Assistant")


# -------------------------
# Load and Process Documents
# -------------------------
@st.cache_resource
def create_vector_store():

    pdf_files = glob.glob(f"{DATA_PATH}/*.pdf")

    if len(pdf_files) == 0:
        st.error("No PDF files found inside data folder")
        st.stop()

    documents = []

    for pdf in pdf_files:
        loader = PyPDFLoader(pdf)
        docs = loader.load()
        documents.extend(docs)

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    # Vector DB
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()

    return vectordb


# -------------------------
# Load RAG Pipeline
# -------------------------
@st.cache_resource
def load_qa_chain():

    vectordb = create_vector_store()

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain


qa_chain = load_qa_chain()


# -------------------------
# Chat Interface
# -------------------------
query = st.text_input("Ask a question about your documents:")

if query:

    with st.spinner("Thinking..."):

        response = qa_chain(query)

        answer = response["result"]
        sources = response["source_documents"]

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for doc in sources:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")

            st.write(f"📄 {source} — Page {page}")
```
