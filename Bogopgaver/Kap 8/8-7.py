"""8-7. Album
Write a function called make_album() that builds a dictionary describing a music album. The function should take in an
 artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the
  function to make three dictionaries representing different albums. Print each return value to show that
  the dictionaries are storing the album information correctly.

Add an optional parameter to make_album() that allows you to store the nubmer of tracks on an album. If the
calling line includes a value for the number of tracks, add that value to the album’s dictionary.
Make at least one new function call that includes the nubmer of tracks on an album."""

def make_album(artist_name, album_title):
   album = {"artist name": artist_name, "title": album_title}
   return album

#creating albums with the function and printing them
album_01 = make_album("jethro tull", "aqualung")
print(album_01)

album_02 = make_album("tv-2", "kys bruden")
print(album_02)

album_03 = make_album("alphaville", "forever young")
print(album_03)

print("########################################")

#Making the function with an optional added parameter for also storing the number of tracks
def make_album_02(artist_name, album_title, tracks = ""):
    if tracks:
        album = {"artist name": artist_name, "title": album_title, "number of tracks": tracks}
    else:
        album = {"artist name": artist_name, "title": album_title}
    return album

#creating an album with no number of tracks indicated.
album_04 = make_album_02("bad religion", "recipe for hate")
print(album_04)

#creating album with number of tracks indicated
album_04 = make_album_02("leonard cohen", "recent songs", 10)
print(album_04)

