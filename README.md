# Beer_calling_bot
from telegram import Update, ParseMode
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = 8179760158:AAHeM7RLjk17aq7ZiH4QeCslZRk80uZtwqQ

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

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tag_all))

app.run_polling()
