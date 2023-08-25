class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if song.genre in Song.genres:
            print("Genre already in list.")
        else:
            Song.genres.append(song.genre)

        Song.add_to_genre_count(song)

    @classmethod
    def add_to_artists(cls, song):
        if song.artist in Song.artists:
            print("Artist already in list.")
        else:
            Song.artists.append(song.artist)

        Song.add_to_artist_count(song)

    @classmethod
    def add_to_genre_count(cls, song):
        if song.genre in Song.genre_count:
            Song.genre_count[song.genre] += 1
        else:
            Song.genre_count.update({song.genre: 1})

    @classmethod
    def add_to_artist_count(cls, song):
        if song.artist in Song.artist_count:
            Song.artist_count[song.artist] += 1
        else:
            Song.artist_count.update({song.artist: 1})
