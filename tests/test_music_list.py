from lib.music_list import *

"""
Check and empty list
"""

def test_music_list_empty_list():
    empty = MusicSheet()
    assert empty.list == []

"""
Add songs to list - 2 songs
"""

def test_music_add_2_songs_to_list():
    songs = MusicSheet()
    songs.add_to_list("Firestone")
    songs.add_to_list("Driver")
    assert songs.list == ["Firestone", "Driver"]

"""
Add songs to list - 4 songs
"""

def test_music_add_4_songs_to_list():
    songs = MusicSheet()
    songs.add_to_list("Hello")
    songs.add_to_list("Livin on a prayer")
    songs.add_to_list("We're the champions")
    songs.add_to_list("APT")
    assert songs.list == ["Hello", "Livin on a prayer", 
                          "We're the champions", "APT"]
