# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

active_tasks = {}


@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📍 قناة تحديثات", url="https://t.me/i2pdfbotchannel"),
        ],
        [
            InlineKeyboardButton("👥 قناة الدعم", url="https://t.me/i2pdfbotchannel"),
            InlineKeyboardButton("👩‍💻 المطور", url="https://t.me/ta_ja199"),
        ] 
   ]
  )
    start_message = (
        "مرحبا!\n\n"
        "أرسل لي ملف مضغوط وسأقوم بفك ضغطه لك."
    )
    await message.reply(start_message, reply_markup=reply_markup)


# Callback query handler
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "فيما يلي الأوامر التي يمكنك استخدامها:\n\n"
        "/start - ابدأ تشغيل الروبوت واحصل على رسالة الترحيب\n"
        "/help - احصل على مساعدة حول كيفية استخدام الروبوت\n\n"
        "لفك ضغط ملف، ما عليك سوى إرسال ملف ZIP إليّ وسأستخرج محتوياته وأرسله إليك مرة أخرى.\n\n"
        "©️ القناة : @i2pdfbotchannel"
    )
    await message.reply(help_message)



@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ تم إلغاء عملية فك الضغط.", show_alert=True)
    else:
        await callback_query.answer("⚠️ لا توجد عملية فك ضغط مستمرة.", show_alert=True)

