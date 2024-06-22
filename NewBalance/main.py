from pyrogram import Client
from pyrogram.types import CallbackQuery
import logging , os 

class DracoChkBot():
    def __init__(self):
        self.app = Client(   
            "DracoChkBot", 
            api_id    = 26209703 ,#API ID de Telegram App 
            api_hash  = '710d72b806f358f502cb1588e148003a',#API Hash de Telegram app 
            bot_token = '6956382268:AAGp_b7FYHJaDoSYyITPL72i5FDZ97iDF58',#Token bot Telegram 
            plugins   =  dict(root="plugins"))

        @self.app.on_callback_query()
        def clod(client, call: CallbackQuery):
            data = call.data.split(":")

            if call.from_user.id != int(data[1]):return call.answer("Botones bloqueados.")
            else: call.continue_propagation()

    def runn(self):
        os.system("cls")
        logging.basicConfig(level=logging.INFO)
        self.app.run()

DracoChkBot().runn()