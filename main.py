import os
from telegram import Update, ParseMode
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def tag_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if '@all' in update.message.text.lower():
        chat = update.effective_chat
        members = await context.bot.get_chat_administrators(chat.id)
        mentions = []

        for member in members:
            user = member.user
            name = user.full_name
            mention = f"[{name}](tg://user?id={user.id})"
            mentions.append(mention)

        text = " ".join(mentions)
        await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tag_all))
    print("Bot is running...")
    app.run_polling()
