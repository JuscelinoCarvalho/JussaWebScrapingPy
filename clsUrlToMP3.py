from youtube_dl import YoutubeDL 


option = 0
audio_downloder = YoutubeDL({'format':'mp3'})



try:
    #audio_downloader.extract_info("https://youtu.be/RF0vVdx2UN8")
    #obj = extract_info("https://youtu.be/RF0vVdx2UN8")
 

except Exception as ex:
    print("Couldn't download the video file audio")
    print("\n" + str(ex))

finally:
    option = int(input("\n1.download again \n2.Exit \n\nOption here: "))

    if option !=1:       
        exit
    pass
pass




#class clsUrlToMP3(object):
#    """description of class"""
#    def __init__(self, urlVideo):
#        self.urlVideo = "https://youtu.be/RF0vVdx2UN8"
        
#    def convertToMP3(self):
#        ###data = urllib.request(self.urlVideo)
#        obj2 = urlopen(self.urlVideo)
#        print(obj2)
#        for line in obj2:
#            print(line)





#obj = clsUrlToMP3("https://youtu.be/RF0vVdx2UN8")
#obj.convertToMP3()
