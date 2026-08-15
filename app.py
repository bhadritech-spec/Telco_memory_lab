import streamlit as st
from anthropic import Anthropic

client = Anthropic()  # reads ANTHROPIC_API_KEY from env

SYSTEM = "You are a concise assistant."


def build_context(user_msg: str) -> list[dict]:
    # THIS is context engineering: you decide exactly what the model sees.
    # Right now it's trivial. It won't stay that way.
    return [
        {"role": "user", "content": user_msg},
    ]


def call_model(system: str, messages: list[dict]) -> str:
    resp = client.messages.create(
        model="claude-sonnet-5",  # model strings change; swap freely
        max_tokens=500,
        system=system,
        messages=messages,
    )
    return resp.content[0].text


st.title("MemoryLab — M1: context by hand")

user_msg = st.text_input("Your message")
if st.button("Send") and user_msg:
    messages = build_context(user_msg)

    with st.expander("Exact context sent to the model", expanded=True):
        st.write("SYSTEM:")
        st.code(SYSTEM)
        st.write("MESSAGES:")
        st.json(messages)

    answer = call_model(SYSTEM, messages)
    st.markdown("**Answer**")
    st.write(answer)
