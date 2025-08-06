import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

openai.api_key = os.getenv("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")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি GPT বট, আমাকে প্রশ্ন করুন।")

async def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = await chatgpt_response(user_input)
    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
