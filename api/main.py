from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import logging
from telegram import Update
from conversations import bh, all_conversations, find_day_conversation
from telegram.ext import CommandHandler, CallbackContext, Updater, ConversationHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
TOKEN = ""


def start(update: Update, context: CallbackContext):
    user = update.effective_user.full_name
    year = datetime.now().year - 8
    _bh = bh._bh(year)
    table =f"{user} የዘንደሮ ማውጫ \n {_bh}"
    bio = BytesIO()
    bio.name = "template_send.png"
    img = Image.open("Back_1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("washrab.ttf", 20)
    draw.text((70, 80), table, (255, 255, 255), font=font)
    img.save(bio, "PNG")
    bio.seek(0)
    update.message.reply_photo(bio,caption="እንኳን ወደ ባህረ ሀሳብ ቴሌግራም ቦት በሰላመ ምጡ")


def help(update: Update, context: CallbackContext):
    update.message.reply_markdown("/all - የሁሉንም አመት ማውጫ ለማግኘት")


def give_table(update: Update, context: CallbackContext):
    year = int(update.message.text)
    update.message.reply_markdown(bh._bh(year=year))


def main():
    global TOKEN
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(all_conversations.all_conversation_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
