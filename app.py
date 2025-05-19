import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def zero_shot_prompt(task, input_text):
    return f"{task}:\n{input_text}"

def one_shot_prompt(task, input_text):
    example = {
        "Summarize": "Summarize:\nThe cat sat on the mat. It was a lazy day.\nSummary: The cat had a lazy day.",
        "Sentiment Analysis": "Sentiment Analysis:\nI love this product, it works like a charm!\nSentiment: Positive"
    }
    return f"{example.get(task, '')}\n\n{task}:\n{input_text}"

def few_shot_prompt(task, input_text):
    example = {
        "Summarize": """Summarize:
The dog barked at night. It kept the neighbors awake.
Summary: The dog disturbed the neighbors at night.

Summarize:
He ate the entire pizza in one go. It was his cheat day.
Summary: He ate a whole pizza on his cheat day.
""",
        "Sentiment Analysis": """Sentiment Analysis:
This phone is terrible, the battery died in 2 hours.
Sentiment: Negative

Sentiment Analysis:
What a beautiful design, I’m in love!
Sentiment: Positive
"""
    }
    return f"{example.get(task, '')}\n\n{task}:\n{input_text}"

def cot_prompt(input_text):
    return f"Question: {input_text}\nLet's think step by step."

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

import gradio as gr

def compare_prompts(task, input_text):
    z_output = get_gemini_response(zero_shot_prompt(task, input_text))
    o_output = get_gemini_response(one_shot_prompt(task, input_text))
    f_output = get_gemini_response(few_shot_prompt(task, input_text))
    cot_output = get_gemini_response(cot_prompt(input_text))
    
    return z_output, o_output, f_output, cot_output

task_options = ["Summarize", "Sentiment Analysis", "General Question"]

demo = gr.Interface(
    fn=compare_prompts,
    inputs=[
        gr.Dropdown(choices=task_options, label="Choose Task"),
        gr.Textbox(lines=4, label="Enter your input text")
    ],
    outputs=[
        gr.Textbox(label="Zero-shot Output"),
        gr.Textbox(label="One-shot Output"),
        gr.Textbox(label="Few-shot Output"),
        gr.Textbox(label="Chain-of-Thought Output")
    ],
    title="🔍 PromptCraft Lab",
    description="Compare how different prompt engineering techniques affect Gemini's responses"
)

if __name__ == "__main__":
    demo.launch()
