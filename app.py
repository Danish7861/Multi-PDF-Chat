import streamlit as st
from dotenv import load_dotenv
from backend.pdf_processor import get_pdf_text, get_text_chunks
from backend.vector_store import get_vector_store
from backend.qa_handler import handle_user_query
import os

load_dotenv()
st.set_page_config("📚 Multi PDF Chatbot", layout="wide", page_icon="🤖")

# Header
st.markdown(
    "<h1 style='text-align: center; color: #2F4F4F;'>📚 Multi-PDF Chat Agent 🤖</h1>",
    unsafe_allow_html=True
)

# Question box
user_question = st.text_input("🔍 Ask something from your uploaded PDFs:")

if user_question:
    with st.spinner("Thinking... 💭"):
        try:
            response = handle_user_query(user_question)
            st.success("Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Sidebar Styling
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        background-color: #1e1e24;
        padding: 25px;
    }

    .sidebar-profile {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .sidebar-profile img {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #4CAF50;
    }

    .upload-section {
        background-color: #2a2d35;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 30px;
    }

    .sidebar-footer {
        text-align: center;
        font-size: 14px;
        color: #cccccc;
        padding-top: 12px;
    }

    .sidebar-footer a {
        color: #ffa500;
        text-decoration: none;
    }

    .sidebar-footer a:hover {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Layout
with st.sidebar:
    st.markdown(
        """
        <style>
        /* Sidebar container */
        section[data-testid="stSidebar"] {
            background-color: #111827;
            padding: 30px 20px;
        }

        /* Profile image style */
        .profile-img-container {
            display: flex;
            justify-content: center;
            margin-bottom: 15px;
        }

        .profile-img-container img {
            border-radius: 12px;
            height: 100px;
            width: 100px;
            object-fit: cover;
            border: 2px solid #4ade80;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }

        /* Upload section */
        .upload-section {
            background-color: #1f2937;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            margin-bottom: 30px;
        }

        .upload-section h4 {
            color: #facc15;
            margin-bottom: 15px;
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #9ca3af;
        }

        .footer a {
            color: #facc15;
            text-decoration: none;
        }

        .footer a:hover {
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Profile image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/img/main.png", width=100)


    # Upload box
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("#### 📁 Upload PDF Files")
    pdf_docs = st.file_uploader("Drag and drop your PDFs here", accept_multiple_files=True, label_visibility="collapsed")
    if st.button("📤 Submit & Process"):
        if pdf_docs:
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                chunks = get_text_chunks(raw_text)
                get_vector_store(chunks)
                st.success("✅ PDF content indexed successfully!")
        else:
            st.warning("⚠️ Please upload at least one file.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <div class="footer">
            Built with ❤️ by <a href="https://github.com/Danish7861" target="_blank">Danish Shahzad</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# Fixed footer
st.markdown(
    """
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #2F4F4F; padding: 10px; color: white; text-align: center; font-size: 13px;">
        📄 Multi-PDF Chatbot | Powered by LangChain, FAISS & Gemini AI
    </div>
    """,
    unsafe_allow_html=True
)
