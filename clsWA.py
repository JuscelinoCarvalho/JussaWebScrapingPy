from supbot import Supbot
from pytube import YouTube

#YouTube('https://www.youtube.com/watch?v=55WBg7GA4l0').streams[0].download()
YouTube("https://www.youtube.com/watch?v=55WBg7GA4l0").streams.last()

class clsWA():
    """Classe para envio e recebimento de mensagens pelo WhatsApp!"""
    def __init__(self):
        pass


    def repeat_message(contact_name="", message="Mensagem Vazia!"):
        Supbot.send_message(contact_name, messagem)
        pass


    with Supbot(mmessage_received=repeat_message) as sbot:
        sbot.wait_for_finish()
        pass


    pass



