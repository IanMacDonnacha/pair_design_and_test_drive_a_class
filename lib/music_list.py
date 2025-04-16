# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

class MusicSheet:
    def __init__(self):
    #paramaters - self
        self.list = []

    def add_to_list(self, songs):
    #parameters - 1 argument songs
        self.list.append(songs)
        return self.list    