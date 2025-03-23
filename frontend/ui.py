import gradio as gr
import requests
import pandas as pd

def display_results():
    response = requests.get("http://127.0.0.1:8000/results").json()
    return (
        pd.DataFrame(response["Extracted News Articles"]),
        pd.DataFrame(response["Sentiment Analysis Results"]),
        ", ".join(response["Common Topics"]) or "None",
        ", ".join(response["Unique Topics"]) or "None",
        f"**Title:** {response['Most Positive/Negative News Article']['Title']}\n"
        f"**Summary:** {response['Most Positive/Negative News Article']['Summary']}\n"
        f"**Sentiment:** {response['Most Positive/Negative News Article']['Sentiment']} (Score: {response['Most Positive/Negative News Article']['Score']:.2f})"
    )

gram_ui = gr.Interface(
    fn=display_results,
    inputs=[],
    outputs=[
        gr.Dataframe(label="Extracted News Articles"),
        gr.Dataframe(label="Sentiment Analysis Results"),
        gr.Textbox(label="Common Topics"),
        gr.Textbox(label="Unique Topics"),
        gr.Textbox(label="Most Positive/Negative News Article")
    ],
    title="Tesla News Sentiment Analysis",
    description="This interface displays Tesla news sentiment analysis, topic overlap, and the most extreme sentiment article."
)

if __name__ == "__main__":
    gram_ui.launch()
