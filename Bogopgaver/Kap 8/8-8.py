"""8-8. User ALbums
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop."""

#function from 8-7:
def make_album(artist_name, album_title, tracks = ""):
    if tracks:
        album = {"artist name": artist_name, "title": album_title, "number of tracks": tracks}
    else:
        album = {"artist name": artist_name, "title": album_title}
    return album

#while loop for a user to enter artists and titles for albums.
while True:
    #introducing the option to quit program
    print("Please note you can quit any time by entering 'q'")
    #prompting for name of artist
    artist = input("Please enter the artist's name: ")
    #checking if the user chose to quit
    if artist.lower() == "q":
        break
    title = input("Please enter the album's name: ")
    # checking if the user chose to quitNo i
    if title.lower() == "q":
        break
    #making the album and printing it
    album = make_album(artist, title)
    print(album)