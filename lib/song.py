class Song():
    count = 0 
    genres = []
    artist = []
    genre_count = []
    artist_count = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genre:
            cls.genres.append(genre)
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artist:
            cls.genres.append(artist)
            cls.genre_count[artist] = cls.artist_count.get(artist, 0) + 1
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in genre:
            genre_count += 1
        else:
            genre_count = 1  


    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in artist:
            artist_count += 1
        else:
            artist_count = 1   

Song = {"Rap": 5, "Rock": 1, "Country": 3}  
Song = {"Beyonce": 17, "Jay-Z": 40}          