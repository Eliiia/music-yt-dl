from mp3_tagger import MP3File as mp3file
import os

dl_folder = "dl" # If you change here, change in dl.py too

print("This program assumes that you have used the download program bundled with this to format your files to use \"AUTHOR - SONG_NAME\".\nIf not, either use that program or manually change the file names to that.\n\nHave fun :)")

albumname = input("What's the album name? ")
f = input(f"Folder name (without / at the end):\n ./{dl_folder}/")

for x in os.listdir(f"{dl_folder}/{f}/"):
    mp3 = mp3file(f"./{dl_folder}/{f}/{x}")
    print(f"\nOPENED {x}")
    
    x = x.replace(".mp3", "")

    s = x.split(" - ")
    print(f"FORMATTED as Artist = '{s[0]}', Song = '{s[1]}'")

    mp3.artist = s[0]
    mp3.song = s[1]
    mp3.album = albumname

mp3.save
print("\nSAVED\n")

input("---\n\nPRESS ENTER TO LEAVE PROGRAM\n")