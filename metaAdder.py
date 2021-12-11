from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

def add_meta(fname, falbum, fnum, ftotal, fdate, fgenre):
    data = fname.split("/")[1].split(" - ")
    data[1] = data[1][:len(data) - 6]
    mp3file = MP3(fname, ID3=EasyID3)
    mp3file['albumartist'] = data[0]
    mp3file['tracknumber'] = str(fnum) + '/' + str(ftotal)
    mp3file['title'] = data[1]
    mp3file['date'] = fdate
    mp3file['genre'] = fgenre
    mp3file['album'] = falbum
    mp3file.save()

if(__name__ == "__main__"):
    print("This cannot be run as a standalone applet")
    exit()