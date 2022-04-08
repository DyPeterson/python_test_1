class Artists:
    artists_seq = 100
    def __init__(self, name, dob, genre):
        self.name = name
        self.dob = dob
        self.genre = genre
        self.artist_id = Artists.artists_seq
        Artists.artists_seq += 1
    def __repr__(self):
        return f"Name:{self.name} Dob:{self.dob} Genre: {self.genre} ID:{self.artist_id}"
class Songs(Artists):
    def __init__(self, title, artist, length, lyrics):
        super().__init__(artist, None, None)
        self.title = title
        self.artist = artist
        self.length = length
        self.lyrics = lyrics
    def __repr__(self):
        if self.artist == Artists.name:
            return f"{Songs.artist} has a song in our database!"
artist1 = Artists("Bob Dylan", "5-24-1942", "Folk")
artist2 = Artists("Paula Abdul", "6-19-1962", "Pop")
artist3 = Artists("Cab Calloway", "12-25-1907", "Jazz")
artist4 = Artists("Jeremy Bolm", "4-06-1983", "Hardcore")
song1 = Songs("The Times They Are A-Changin'","Bob Dylan","3:12","Come gather 'round people Wherever you roam And admit that the waters Around you have grown And accept it that soon You'll be drenched to the bone If your time to you is worth savin' Then you better start swimmin' Or you'll sink like a stone For the times they are a-changin'")
song2 = Songs("Straight Up","Paula Abdul","4:11","Lost in a dream I don't know which way to go. (A-let me say it.) If you are all that you seem Then, baby, I'm movin' way too slow.")
song3 = Songs("Mama Tried","Merle Haggard","2:14","The first thing I remember knowing Was a lonesome whistle blowing And a young'un's dream of growing up to ride On a freight train leaving town Not knowing where I'm bound And no one could change my mind but Mama tried")
artist_dict = {
    artist1.artist_id : artist1,
    artist2.artist_id : artist2,
    artist3.artist_id : artist3,
    artist4.artist_id : artist4,
}
artist_name1 = getattr(artist1, 'name')
artist_name2 = getattr(artist2, 'name')
artist_name3 = getattr(artist3, 'name')
artist_name4 = getattr(artist4, 'name')
song_artist1 = getattr(song1, "artist")
song_artist2 = getattr(song2, "artist")
song_artist3 = getattr(song3, "artist")
def valid_artist():
    value = input("Search for an artist")
    if value == artist_name1:
        return True
    elif value == artist_name2:
        return True
    elif value == artist_name3:
        return True
    elif value == artist_name4:
        return True
    return False
def valid_song():
    if artist_name1 == song_artist1:
        return artist_name1
    elif artist_name2 == song_artist2:
        return artist_name2
    return False
valid_song()
valid_artist()