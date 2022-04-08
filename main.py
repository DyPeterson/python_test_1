class Artists:
    artist_seq = 10
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


artist1 = Artists("Bob Dylan", "5-24-1942", "Folk",)
artist2 = Artists("Paula Abdul", "6-19-1962", "Pop")
artist3 = Artists("Cab Calloway", "12-25-1907", "Jazz")
artist_dict = {
    Artists.artist_seq : "Bob Dylan",
    Artists.artist_seq : "Paula Abdul",
    Artists.artist_seq : "Cab Calloway",
}
# print(Artists.artist_id)
print(artist1)
Artists.art_print(artist1)
Artists.art_print(artist2)