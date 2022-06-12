import os
import pytube   
import ssl
from enum import Enum
from moviepy.editor import *
from pydub import AudioSegment


ssl._create_default_https_context = ssl._create_unverified_context
os.environ["PYTHONHTTPSVERIFY"] = "0"


class enumCodec(Enum):
    MP4 = 0
    MP3 = 1
    pass


class clsConvertToMP3():
    """description of class"""

    def __init__(self, strPathFrom, strPathToMP3="C:\\Users\\All Users\\tmpDownloads\\Youtube\\MP3s\\"):
        self.strPathFrom = strPathFrom
        self.strPathToMP3 = strPathToMP3
        pass


    def fConvertToMP3(self, nomeMusica):
        #video = VideoFileClip(self.strPathFrom + "Lionel Richie - Stuck On You (Lyrics).mp4")
        #video.audio.write_audiofile(self.strPathToMP3 + "Lionel Richie - Stuck On You.mp3")
        
        #video = VideoFileClip(self.strPathFrom + nomeMusica)
        print(nomeMusica)
        video = VideoFileClip("https://youtu.be/RF0vVdx2UN8")


        video.audio.write_audiofile(self.strPathToMP3 + str(nomeMusica).replace(".mp4",".mp3"))
        pass

    pass #FIM da clsConverToMP3



class clsSplitMP3():

    def __init__(self, mp3FilePath, timeLeft=0, timeRight=0):
        self.mp3FilePath = mp3FilePath
        self.timeLeft = timeLeft
        self.timeRight = timeRight
        pass #init
        
    def fSplit(self):
        f = open(self.mp3FilePath, "r")
        AudioSegment.converter("C:\\Program Files (x86)\\ffmpeg\\bin\\ffmpeg.exe")
        song = AudioSegment.from_mp3(f.name)#####self.mp3FilePath)
        tamanho = len(song)
        pass #split

    pass #clsSplitMP3

musicas = [] #Videos URLs List
#musicas.append("https://www.youtube.com/watch?v=I8aFBeeIJ9I&list=LLdqpsVo0_PM6XqTaGWQDJHw&index=175")  #Cyndi Lauper - I Drove All Night (from Live...At Last)
#musicas.append("https://www.youtube.com/watch?v=ZONKoKIQ9RY&list=PL6iiuyiigcqP5f-l7Kdgq5K0QC5vxtS-d&index=3&t=0s")  #Cyndi Lauper - All Through the Night (Official Audio)
#musicas.append("https://www.youtube.com/watch?v=SECVGN4Bsgg&list=RDIbsfupH8W1o&index=25")  #Men At Work - Who Can It Be Now? (Video Version)
#musicas.append("https://www.youtube.com/watch?v=HoXLyIzVnIo")  #Bonnie Tyler - Total Eclipse of the Heart - (2ª Versão 1983) Tradução
#musicas.append("https://www.youtube.com/watch?v=42xkHtUUIZs")  #Men At Work - Down Under (Video)
#musicas.append("https://www.youtube.com/watch?v=djV11Xbc914")  #a-ha - Take On Me (Vídeo oficial)
#musicas.append("https://www.youtube.com/watch?v=3wxyN3z9PL4")  #Starship - Nothing's Gonna Stop Us Now (Official Music Video)
#musicas.append("https://www.youtube.com/watch?v=ogoIxkPjRts")  #Air Supply - Making Love Out Of Nothing At All
#musicas.append("https://www.youtube.com/watch?v=iyIOl-s7JTU")  #ABBA - The Winner Takes It All (1980) HD 0815007
#musicas.append("https://www.youtube.com/watch?v=XEjLoHdbVeE&list=PLCqEj-8qXe2iC_N9z3hO-_2zPWD4jkYuI&index=325")  #ABBA - Gimme! Gimme! Gimme! (A Man After Midnight)
#musicas.append("https://www.youtube.com/watch?v=w46bWxS9IjY")  #Rod Stewart - I Don't Want To Talk About It (from One Night Only! Live at Royal Albert Hall)
#musicas.append("https://www.youtube.com/watch?v=SvCyFHWBUlc")  #Tina Turner - The Best - Ao Vivo Wembley (HD 1080p)
#musicas.append("https://www.youtube.com/watch?v=A7xcGYQlGL4")  #Reencarnação de Janis Joplin?
#musicas.append("https://www.youtube.com/watch?v=_7sJl4TUqQg")  #14 Y.O Rock Star Is BACK With An Original on AGT Champions | Got Talent Global
#musicas.append("https://www.youtube.com/watch?v=1eNSWZ4x2ZU")  #Whiskey Blues | Best of Slow Blues/Rock #1
musicas.append("https://www.youtube.com/watch?v=55WBg7GA4l0")  # Musica do Uly

#conv = clsConvertToMP3(strPathFrom="E:\\",strPathToMP3="E:\\MP3\\")
conv = clsConvertToMP3("C:\\Users\\All Users\\tmpDownloads\\Youtube\\", "C:\\Users\\All Users\\tmpDownloads\\Youtube\\MP3s\\")

conv.fConvertToMP3("TesteJK.mp3")

#for m in musicas:
#    youtube = pytube.YouTube(m)
#    video = youtube.streams.first()
#    video.download("E:\\")
#    #conv.fConvertToMP3(m)
#    pass #For


#files = os.listdir("E:\\")

#for f in files:
#    if f != "System Volume Information" and f != "MP3":
#        conv.fConvertToMP3(f)
#        pass #If
#    pass #Files

###### E:\\MP3\\14 YO Rock Star Is BACK With An Original on AGT Champions  Got Talent Global.mp3

#mSplited = clsSplitMP3("E:\\MP3\\14YORockStarIsBACKWithAnOriginalonAGTChampionsGotTalentGlobal.mp3", 315000000, 523000000)
#mSplited.fSplit()
