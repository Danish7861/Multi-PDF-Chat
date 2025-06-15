from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

def get_conversational_chain():
    template = """
    Answer the question from the provided context. If unavailable, say "Answer not available in the context."

    Context:
    {context}

    Question:
    {question}

    Answer:"""

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)
