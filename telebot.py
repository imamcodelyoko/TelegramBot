from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#token
TOKEN: Final = '7789350263:AAG6rtiBSV6y_eTHhenZJMJggPdhEbB1f5M'
BOT_USERNAME: Final = '@premiereinfo_bot'

#Command awal(MENU)
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo!👋 Selamat datang di Pribadi Premiere School Info Bot. \n"
        "<b>Kindergarten | Elementary | Middle | High</b> \n\n"
        "Ketuk <i>menu</i> untuk mengetahui informasi tentang Pribadi Premiere School!", parse_mode="HTML")

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>Pendaftaran Online</b>: \n"
        "https://pribadipremiere.sch.id/form/", parse_mode="HTML")

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Contact us directly: \n"
        " <b>Location</b> \n"
        "📍 Jl. Boulevard Grand Depok City, Kec. Sukmajaya, Kota Depok, Jawa Barat 16412 \n\n"
        " <b>Email</b> \n"
        "📧 admin.premiere@pribadidepok.sch.id \n" 
        "📧 info.premiere@pribadidepok.sch.id \n\n" 
        " <b>Phone</b>\n"
        "📞 +(62)-812-3233-1995", parse_mode="HTML")

async def socialmedia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        " <b>Follow our social media</b> \n\n"
        "Facebook: Pribadi Premiere School \n"
        "Instagram: instagram.com/pribadipremiereschool \n"
        "Youtube: https://www.youtube.com/@PribadiPremiereSchool95 \n"
        "Website: https://pribadipremiere.sch.id/", parse_mode="HTML")

async def schools_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>Our Education Program:</b> \n\n"
        "Kindergarten🧸 \n  https://zynthink.github.io/KindergartenPribadiPremiere/ \n\n"
        "Elementary📚 \n https://zynthink.github.io/ElementaryPribadiPremiere/ \n\n"
        "Junior High School📖 \n https://zynthink.github.io/JuniorHighSchoolPribadiPremiere/ \n\n"
        "Senior High School🎓 \n  https://zynthink.github.io/JuniorHighSchoolPribadiPremiere/", parse_mode="HTML")

async def aboutus_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        "<b>Pribadi Premiere School</b> is a private institution offering an international standard of education through the Cambridge and National Curriculums, established in 2023, and located on Jalan Blv Grand Depok City (GDC) in Depok as Education City.\n\n"
        "<b>Pribadi Premiere School</b> is committed to guide the generation who are morally upright, intellectually capable, globally aware, and culturally enriched. \n\n"
        "<b>Visi:</b> \n"
        "Menjadi sekolah mandiri bagi terwujudnya generasi emas, berakhlak mulia, cerdas, berwawasan global dan berbudaya. \n\n"
        "<b>Misi:</b> \n"
        "1. Mengembangkan etos kerja yang penuh kemandirian dalam merancang dan mengelola sumber daya yang dimiliki.\n"
        "2. Menghasilkan generasi emas yang memiliki akhlak mulia dan memegang teguh norma-norma yang dapat diaktualisasikan dalam kehidupan bermasyarakat.\n"
        "3. Mengembangkan kapasitas dan kualitas warga sekolah dalam bidang ilmu pengetahuan dan teknologi.\n"
        "4. Meningkatkan standar mutu pendidikan yang unggul dalam menghadapi persaingan global.\n"
        "5. Menumbuhkembangkan sikap cinta tanah air dan budaya bangsa kepada segenap warga sekolah.\n\n"
        "Ketuk /contact untuk menghubungi sekolah.", parse_mode="HTML")

#RESPON dari KEYWORD yang di input user
def handle_response(text: str):
    processed: str = text.lower()

    if 'assalamualaikum' in processed: #processed: user tidak akan masalah input huruf besar/kecil
        return "Halo, walaikumsallam" 
    if 'prestasi' in processed:
        return "Sekolah Premiere telah meraih berbagai prestasi akademik dan non-akademik. Cek /socialmedia untuk mengetahui lebih lanjut."
    if 'terima kasih' in processed:
        return 'Dengan senang hati. 😊'
    
    return 'Maaf, perintah tidak dikenali bot. \n\n Ketuk /contact untuk pertanyaan lebih lanjut!'

#handle message, pengecekan message datang dari chat pribadi/grup
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)
        
    print('Bot : ', response)
    await update.message.reply_text(response)

#Function cek error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update : {update} caused error {context.error}')

if __name__ == '__main__':
    print('memulai bot..')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('contact', contact_command))
    app.add_handler(CommandHandler('schools', schools_command))
    app.add_handler(CommandHandler('aboutus', aboutus_command))
    app.add_handler(CommandHandler('socialmedia', socialmedia_command))
    app.add_handler(CommandHandler('info', info_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Pools the bot 
    print('Bot sedang berjalan...')
    app.run_polling(poll_interval=3)
