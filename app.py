import streamlit as st
from transformers import pipeline
from groq import Groq

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Assistant Comparison",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stChatMessage {
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🤖 AI Assistant Comparison")
st.write("Compare an Open Source Assistant and a Frontier Model Assistant")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Assistant Settings")

model_choice = st.sidebar.selectbox(
    "Choose Assistant",
    [
        "Open Source (Qwen2.5)",
        "Frontier Model (Groq)"
    ]
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------- SESSION MEMORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY OLD MESSAGES ----------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- LOAD OPEN SOURCE MODEL ----------------

@st.cache_resource
def load_oss_model():
    generator = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct"
    )
    return generator

# ---------------- GROQ CLIENT ----------------

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

# ---------------- USER INPUT ----------------

user_input = st.chat_input("Type your message here...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):

        # ---------------- OPEN SOURCE MODEL ----------------

        if model_choice == "Open Source (Qwen2.5)":

            generator = load_oss_model()

            prompt = f"""
You are a helpful AI assistant.

User: {user_input}
Assistant:
"""

            response = generator(
                prompt,
                max_new_tokens=300,
                do_sample=True,
                temperature=0.7,
                truncation=True
            )

            reply = response[0]["generated_text"]

            # Clean output
            if "Assistant:" in reply:
                reply = reply.split("Assistant:")[-1].strip()

        # ---------------- FRONTIER MODEL ----------------

        else:

            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant."
                    },
                    *st.session_state.messages
                ],
                temperature=0.7,
                max_tokens=300
            )

            reply = completion.choices[0].message.content

        # Show response
        st.markdown(reply)

        # Store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })