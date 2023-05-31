from . import bh
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)

ACCEPT_ALL_MESSAGE = 0


def all(update: Update, context: CallbackContext):
    update.message.reply_markdown("ማውጫውን ለማግኘት ዓመተ ምህረቱን ያስገቡ")
    return ACCEPT_ALL_MESSAGE


def send_all(update: Update, context: CallbackContext):
    year = update.message.text
    while True:
        try:
            year = int(year)
            break
        except:
            update.message.reply_text(f"{year} ቁጥር አይደለም ቁጥር ያስገቡ")
    table = bh._bh(year)
    bio = BytesIO()
    bio.name = "template_send.png"
    img = Image.open("Back_1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("zelan.ttf", 20)
    draw.text((70, 90), table, (255, 255, 255), font=font)
    img.show()
    img.save(bio, "PNG")
    bio.seek(0)
    update.message.reply_photo(bio)
    return ConversationHandler.END


all_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("all", all)],
    states={
        ACCEPT_ALL_MESSAGE: [MessageHandler(Filters.text & ~Filters.command, send_all)],
    },
    fallbacks=[],
)
