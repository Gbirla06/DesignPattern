'''
    📖 Example 2: Media Player Adapter 🎵
        Imagine we have a Media Player that supports MP3 format, but we receive MP4 files.

    Steps :
        🚀 Step 1: Define the Existing Class (MP4 Player)
        🚀 Step 2: Define the Expected Interface (Target)
        🚀 Step 3: Create the Adapter
        🚀 Step 4: Client Uses Adapter

'''

from abc import ABC, abstractmethod

# 🚀 Step 1: Define the Existing Class (MP4 Player)
class MP4Player :
    """ Adaptee : Plays MP4 files """

    def play_mp4(self, filename) :
        return f"Playing MP4 file : {filename}"


# 🚀 Step 2: Define the Expected Interface (Target)
class MediaPlayer(ABC) :
    """ Target Interface: Expects play_audio() method """

    @abstractmethod
    def play_audio(self, filename):
        pass


# 🚀 Step 3: Create the Adapter
class MP4toMP3Adaper(MediaPlayer) :

    def __init__(self, mp4_player : MP4Player) :
        self.mp4_player = mp4_player
    
    def play_audio(self, filename) :
        return self.mp4_player.play_mp4(filename)
    
# 🚀 Step 4: Client Uses Adapter
def client_heper(file_name) :

    mp4_player = MP4Player()
    adapter = MP4toMP3Adaper(mp4_player)
    play_audio_output = adapter.play_audio(file_name)
    print(play_audio_output)

if __name__ == "__main__" :
    file = input("Enter mp4 file name with .mp4 extension : ")
    client_heper(file)
