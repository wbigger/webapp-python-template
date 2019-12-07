class Song:
    def __init__(self, title, author, feat, album, length, year, url):
        self.title = title
        self.author = author
        self.feat = feat
        self.album = album
        self.length = length
        self.year = year
        self.url = url


song_1 = Song("Bassotto", "Tony Effe 777", "DPG", "Singolo",
              1.58, 2019, "https://youtu.be/Hv4GCqUgXUE")
song_2 = Song("Livin' La Vida Loca", "Ricky Martin", "self",
              "Singolo", 4.03, 1999, "https://youtu.be/p47fEXGabaY")
song_3 = Song("SW1N6O", "Tha Supreme", "Salmo", "236451",
              3.04, 2019, "https://youtu.be/HyazQiEEXO0")
song_4 = Song("Monster Inc", "Disney", "self", "Disney Music", 2.10,
              2002, "https://youtu.be/aMwSNDRP90o")
song_5 = Song("Giorno Theme RMX", "JoJo's Bizarre Adventure",
              "self", "SoundTracks", 2.31, 2019, "https://youtu.be/EA9GnGwYTJg")
song_6 = Song("L'Amour Toujours", "Gigi D'Agostino", "self",
              "Singolo", 4.02, 1999, "https://youtu.be/w15oWDh02K4")
song_7 = Song("Immigrato", "Checco Zalone", "self", "Tolo Tolo",
              2.58, 2019, "https://youtu.be/SmH2ZZy0dUI")
songlist = [song_1, song_2, song_3, song_4, song_5, song_6, song_7]
