import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from constants import groq_key

# Initialize LLM
llm = ChatGroq(api_key=groq_key, model_name="deepseek-r1-distill-llama-70b")

st.set_page_config(page_title="CodePilot", page_icon="🤖")
st.title("CodePilot")

# Programming language selectbox
language = st.selectbox(
    "Choose programming language:",
    ["Python", "JavaScript", "Java", "C++", "HTML", "C#", "Go", "Rust", "TypeScript", "Ruby"]
)

# Code context input
code_context = st.text_area("Paste your code here (optional):", height=200)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding assistant. The user is working with {language} code. If code is provided, use it to give accurate, concise, and helpful responses."),
    ("human", "Code:\n{code_context}\n\nQuestion:\n{question}")
])

# LLMChain setup
chain = LLMChain(llm=llm, prompt=prompt)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
question = st.text_input("Ask a question about your code:")

# ✅ Generate button
if st.button("Generate"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = chain.invoke({
                "language": language,
                "code_context": code_context,
                "question": question
            })
            st.session_state.chat_history.append(("You", question))
            st.session_state.chat_history.append(("Assistant", response["text"]))

# Display chat history
    st.subheader("🔍 Chat History")
    for role, msg in st.session_state.chat_history[::-1]:
        if role == "You":
            st.subheader(f"**🧑 You:** {msg}")
        else:
            st.subheader(f"**🤖 Assistant:** {msg}")
