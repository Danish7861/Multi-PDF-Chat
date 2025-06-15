from .vector_store import load_vector_store
from .conversational_chain import get_conversational_chain

def handle_user_query(query):
    vector_store = load_vector_store()
    docs = vector_store.similarity_search(query)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
    return response["output_text"]
