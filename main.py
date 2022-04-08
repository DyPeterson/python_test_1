class Artists:
    artist_id = 10
    def __init__(self, name, dob, genre, artist_id):
        self.name = name
        self.dob = dob
        self.genre = genre
        self.artist_id = artist_id
        if artist_id in Artists.artist_id:
            Artists.artist_id += 1
        else:
            artist_id = Artists.artist_id
class Songs:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics
print(Artists.artist_id)