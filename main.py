class Artists:
    artist_seq = 100
    def __init__(self, name, dob, genre):
        self.name = name
        self.dob = dob
        self.genre = genre
        self.artist_id = Artists.artist_seq
        Artists.artist_seq += 1

    def art_print(self):
        print(f"ID:{self.artist_id}")

class Songs:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics
        # check if self.artist is = Artists.name
        # print the artists name and say it exists in the database.


artist1 = Artists("Bob Dylan", "5-24-1942", "Folk",)
artist2 = Artists("Paula Abdul", "6-19-1962", "Pop")
artist3 = Artists("Cab Calloway", "12-25-1907", "Jazz")
artist4 = Artists("Jeremy Bolm", "4-06-1983", "Hardcore")
song1 = Songs("The Times They Are A-Changin'","Bob Dylan","3:12","Come gather 'round people Wherever you roam And admit that the waters Around you have grown And accept it that soon You'll be drenched to the bone If your time to you is worth savin' Then you better start swimmin' Or you'll sink like a stone For the times they are a-changin'")
song2 = Songs("Straight Up","Paula Abdul","4:11","Lost in a dream I don't know which way to go. (A-let me say it.) If you are all that you seem Then, baby, I'm movin' way too slow.")
song3 = Songs("Mama Tried","Merle Haggard","2:14","The first thing I remember knowing Was a lonesome whistle blowing And a young'un's dream of growing up to ride On a freight train leaving town Not knowing where I'm bound And no one could change my mind but Mama tried")
artist_dict = {
    Artists.artist_seq : "Bob Dylan",
    Artists.artist_seq : "Paula Abdul",
    Artists.artist_seq : "Cab Calloway",
}
# print(Artists.artist_id)
print(artist1)
Artists.art_print(artist1)
Artists.art_print(artist2)
Artists.art_print(artist3)
Artists.art_print(artist4)