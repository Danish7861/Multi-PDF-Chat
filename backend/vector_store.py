from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

def get_vector_store(text_chunks, folder="faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    store = FAISS.from_texts(text_chunks, embedding=embeddings)
    store.save_local(folder)

def load_vector_store(folder="faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return FAISS.load_local(folder, embeddings, allow_dangerous_deserialization=True)
