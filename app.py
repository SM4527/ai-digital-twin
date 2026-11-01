import os
import spaces
from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

groq_api_key = os.getenv("GROQ_API_KEY")

if groq_api_key:
    print("Groq API Key exists")
else:
    print("Groq API Key not set and this is required")

groq_url = "https://api.groq.com/openai/v1"

groq = OpenAI(api_key=groq_api_key, base_url=groq_url)

MODEL_NAME = "openai/gpt-oss-20b"

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


@spaces.GPU
def zero_gpu_placeholder():
    """Never called. ZeroGPU Spaces refuse to start without at least one @spaces.GPU function."""


def to_openai(history):
    """Convert Gradio history to plain role/content messages accepted by Groq."""
    return [
        {"role": m["role"], "content": "".join(c["text"] for c in m["content"] if c["type"] == "text")}
        for m in history
    ]


def chat(message, history):
    messages = system + to_openai(history) + [{"role": "user", "content": message}]
    response = groq.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = groq.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
