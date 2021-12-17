#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
bot = ChatBot("Python-BOT")
trainer = ListTrainer(bot)
trainer.train(['apa nama kamu?', 'nama saya Python-BOT'])
trainer.train(['siapa nama kamu?', 'saya adalah BOT'])
trainer.train(['hai','hallo','hei','hello'])
trainer.train(['cara absensi','pertama buka aplikasi terus klik tombol absensi hadapkan wajah kekamera','bagaimana untuk absensi','buka aplikasi terus klik tombol absensi hadapkan wajah kekamera'])
trainer.train(['mengatasi gagal absensi','mohon ditunggu sebentar','gagal absensi', 'segera chat ke admin'])
trainer.train(['rekap bermasalah gagal','segera diperbaiki','laporan gagal bermasalah','mohon tunggu'])
trainer.train(['wajah tidak dikenali','coba ulangi lagi','nama tidak sesuai wajah','hubungi admin'])
trainer.train(['aplikasi lelet','tunggu sebentar'])
trainer.train(['terimakasih','baik','okeh', 'oke'])
trainer.train(['apa fitur yang ada pada web','absensi wajah,dan chatbot '])
trainer.train(['dimana menu chatbot','dibagian menu help','di menu icon pesan'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.indonesia")
@app.route("/")
def index():    
    return render_template("index.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
