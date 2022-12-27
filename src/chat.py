import openai
from telegram import Update
from telegram.ext import CallbackContext


def open_ai_response(input_string):
    openai.api_key_path = "open_ai_api.txt"
    model_engine = "text-davinci-002"

    prompt = (f"{input_string}")
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    message = completions.choices[0].text
    return message

def chat_response(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(open_ai_response(update.message.text))