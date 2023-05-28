from . import bh
from telegram import Update
from telegram.ext import ConversationHandler,CallbackContext,CommandHandler,MessageHandler,Filters
ACCEPT_ALL_MESSAGE =0
def all(update:Update,context:CallbackContext):
    update.message.reply_markdown("ማውጫውን ለማግኘት ዓመተ ምህረቱን ያስገቡ")  
    return ACCEPT_ALL_MESSAGE
def send_all(update:Update,context:CallbackContext):
    year = update.message.text
    while (True):
        try:
            year = int(year)
            break
        except:
            update.message.reply_text(f"{year} ቁጥር አይደለም ቁጥር ያስገቡ")
    message = bh._bh(year)
    update.message.reply_text(message)
    return ConversationHandler.END
all_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("all",all)],
    states={
        ACCEPT_ALL_MESSAGE:[MessageHandler(Filters.text&~Filters.command,send_all)],
    },
    fallbacks=[],
)