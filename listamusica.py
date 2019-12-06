class Song:
    def __init__(self, title, author, feat, album, length, year):
        self.title = title
        self.author = author
        self.feat = feat
        self.album = album
        self.length = length
        self.year = year

song_1 = Song("BASSOTTO", "DPG", "", "BASSOTTO", 1.58, 2019) 
song_2 = Song("LIVIN' LA VIDA LOCA", "RICKY MARTIN", "", "", 4.03, 1999)
song_3 = Song("SW1N6O", "Tha Supreme", "Salmo", "236451", 3.04, 2019)

songlist = [song_1, song_2, song_3]