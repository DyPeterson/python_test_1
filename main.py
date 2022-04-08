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
    def art_print(self):
        print(f"Name:{self.name} Dob:{self.dob} ID:{self.artist_id}")
        return self.artist_id

class Songs:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics
        # check if self.artist is = Artists.name
        # if self.artist == Artists.name:
        #   print(f"{self.artist} has a song in our database!")
        # # print the artists name and say it exists in the database.
        # else:
        #     print(f"Sorry no songs for {self.artist} exists in our database")



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
# for artist in artist_dict:
#     name = artist1.name
#     dob = artist1.dob
#     genre = artist1.genre
    # Artists.art_print(artist)
print(artist_dict)
# for key in artist_dict:
#     artist = Artists(name, dob, genre)
#     artist_id = f"{key}"
#     print(key)