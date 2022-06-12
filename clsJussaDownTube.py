import pytube
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip




class clsJussaDownTube():
    """description of class"""

    def __init__(self, path, strVideoPath):
        self.path = path
        self.strVideoPath = strVideoPath
        pass
    


    def GetAllData(self):
        vUrl = self.strVideoPath
        vTube = pytube.YouTube(vUrl)
        vd = vTube.streams.first()
        vd.download(self.path)

        print(vd.title)
        print(vd.video_id)
        print(vd.age_restricted)

        print("------------------------------------- STREAMS -----------------------------------------")
        strm = vd.streams.all()
        for i in streams:
            print(i)

        pass

    def splitVideo(self):
        vSub = ffmpeg_extract_subclip
        vVideo = self.strVideoPath
        times = []
        times.append(59)
        times.append(83)
        
        vSub(vVideo,times[0], times[1], self.strVideoPath)

    pass

print("Os videos serao salvos no caminho abaixo: /n")
print(os.path.dirname(pytube.__file__))
#obj = clsJussaDownTube(strVideoPath="https://www.youtube.com/watch?v=82BIdzwZbs4")
obj = clsJussaDownTube("C:\\ProgramData\\tmpDownloads\\Youtube\\", "https://youtu.be/RF0vVdx2UN8")
obj.GetAllData()
#obj.splitVideo()