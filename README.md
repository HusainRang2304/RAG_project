# RAG Knowledge Assistant — Explanation
## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline that enables users to query PDF documents using natural language.

The system retrieves relevant document chunks using semantic search and generates answers using a Large Language Model (LLM).

## Architecture
```
 </>Code

PDF Documents
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Embeddings (Vector Representation)
      ↓
Chroma Vector Database
      ↓
User Query
      ↓
Similarity Search
      ↓
LLM (GPT)
      ↓
Final Answer + Sources
```

## Components Explained
### 1. Document Loader
```
PyPDFLoader
```

Loads PDF files and converts them into text documents.

### 2. Text Splitter
```
RecursiveCharacterTextSplitter
```

Splits large text into smaller chunks to improve retrieval accuracy.

**Why?**  ->  LLMs perform better with smaller context windows.

### 3. Embeddings
```
OpenAIEmbeddings
```

Converts text into vectors representing semantic meaning.

This allows similarity search instead of keyword search.

### 4. Vector Database
```
Chroma
```
Stores embeddings and enables fast semantic retrieval.

### 5. Retriever
```
vectordb.as_retriever()
```
Finds the most relevant chunks for a user question.

### 6. Language Model
```
ChatOpenAI
```
Generates answers using retrieved context.

### 7. RetrievalQA Chain
```
RetrievalQA.from_chain_type()
```
Combines retrieval + generation into one pipeline.

### 8. Streamlit UI
Provides a simple web interface for interaction.

## Key Features
```
Multi-document support
Source citations
Persistent vector database
Semantic search
LLM-powered responses
Interactive UI
```

## Performance Considerations
```
For production systems:
Use Pinecone / Weaviate
Add caching
Use hybrid search
Add reranking
Deploy via Docker
Add authentication
```
## Future Improvements
```
Chat memory
Document upload UI
FastAPI backend
AWS deployment
Multi-user support
Evaluation metrics
```
