import base64
import streamlit as st
from openai import OpenAI

openai = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1/")
# model = "llava:13b"
model = "llama3.1:8b"


def get_response():
    response = openai.chat.completions.create(
        model=model,
        messages=st.session_state.message_history,
        stream=True,
        temperature=0.2,
    )
    for chunk in response:
        yield chunk.choices[0].delta.content


# Initialize session state
if "message_history" not in st.session_state:
    st.session_state.message_history = []

# Main app
st.title("LLM Chat App")

# System prompt field
s_prompt = """You are Neo a helpful coding assistant. You are a Python expert and a great software architect. You help intermediate coders with code reviews."""
system_prompt = st.text_area("System Prompt", height=100, value=s_prompt)
if (
    system_prompt
    and {"role": "system", "content": system_prompt}
    not in st.session_state.message_history
):
    st.session_state.message_history.append(
        {"role": "system", "content": system_prompt}
    )

if reset_button := st.button("Reset Chat", use_container_width=True):
    st.session_state.message_history = []
    uploaded_image = None
    st.rerun()

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        if isinstance(message["content"], list):
            st.image(
                base64.b64decode(
                    message["content"][1]["image_url"]["url"].removeprefix(
                        "data:image/jpeg;base64,"
                    )
                ),
                caption=message["content"][0]["text"],
            )
        else:
            st.markdown(message["content"])

# Image upload field
uploaded_image = st.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

# User input field
if user_input := st.chat_input("Your Message"):
    if uploaded_image:
        img_bytes = [img.read() for img in uploaded_image]
        b64_imgs = [base64.b64encode(img).decode("utf-8") for img in img_bytes]
        content = [{"type": "text", "text": user_input}]
        for img in b64_imgs:
            content.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img}",
                        "detail": "high",
                    },
                }
            )
        st.session_state.message_history.append(
            {
                "role": "user",
                "content": content,
            }
        )
        with st.chat_message("user"):
            if len(uploaded_image) == 1:
                st.image(uploaded_image, caption=user_input, use_column_width=True)
            else:
                st.image(uploaded_image)
    else:
        st.session_state.message_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

    with st.chat_message("assistant"):
        response = st.write_stream(get_response())

    # Append LLM response to message history
    st.session_state.message_history.append({"role": "assistant", "content": response})
