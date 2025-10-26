from telegram import Update, Document
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ⚠️ ХАРДКОД — токен вписан прямо в код
BOT_TOKEN = "8209923052:AAEuTEsfNOTyQO5E18EATMun-G78kLuzpFU"

# Разрешённые пользователи (теперь с твоим ID)
ALLOWED_USERS = ["346434851"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Жду Excel файл.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    if user_id not in ALLOWED_USERS:
        return await update.message.reply_text("У тебя нет доступа к загрузке.")

    document: Document = update.message.document

    # --- здесь потом будет логика проверки файла --- #

    await update.message.reply_text(f"Файл {document.file_name} принят. Проверка позже будет добавлена.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    app.run_polling()

if __name__ == "__main__":
    main()

