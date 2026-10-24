"""MSAI-631 Week 1: Hello World on Hugging Face Spaces.

A minimal Gradio app that confirms the development environment works.
It is built with gr.Blocks so it can grow into the Week 3 chatbot.
"""
import platform
import gradio as gr


def greet(name: str) -> str:
    name = (name or "").strip() or "World"
    return f"Hello, {name}! Your MSAI-631 development environment is running."


def env_info() -> str:
    return (
        f"Python {platform.python_version()} | "
        f"Gradio {gr.__version__} | "
        f"{platform.system()}"
    )


with gr.Blocks(title="MSAI-631 Hello World") as demo:
    gr.Markdown("# MSAI-631 Hello World\nOyin Akpe, University of the Cumberlands")
    name_box = gr.Textbox(label="Your name", placeholder="Type a name and press Greet")
    greet_btn = gr.Button("Greet", variant="primary")
    output = gr.Textbox(label="Response")
    gr.Markdown(f"**Environment:** {env_info()}")
    greet_btn.click(greet, inputs=name_box, outputs=output)
    name_box.submit(greet, inputs=name_box, outputs=output)

if __name__ == "__main__":
    demo.launch()
