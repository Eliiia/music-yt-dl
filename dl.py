from pytube import Playlist, YouTube
import os

dl_folder = "dl" # If you change here, change in format.py too

p = Playlist(input("Enter playlist link:\n "))
f = input(f"Folder name (without / at the end):\n ./{dl_folder}/")
print('\nNumber of videos in playlist: %s' % len(p.video_urls))

x = 1

for url in p.video_urls:
    yt = YouTube(url)
    t = yt.streams.filter(only_audio=True)
    t[0].download(f"{dl_folder}/{f}/")

    print(f"DOWNLOADED {x}: {url}")
    x = x+1

print("\nDone!\n")

inp = input("Would you like to format your songs' names and convert to mp3? (will crash without ffmpeg) (y/n)\n ")
if inp == "Y" or inp == "y" or inp == "yes":
    print("\nFiles will be named 'ARTIST - SONG_NAME'. I hope that's ok with you.\n")
    artist = input("What is the artist name?\n ")
    
    for x in os.listdir(f"{dl_folder}/{f}/"):
        print(f"\nFILE NAME: {x}")
        song = input("What's the name of the song ('SKIP' to delete the file)? ")
        
        if(song == "SKIP" or song == "skip"):
            os.system(f'rm ./{dl_folder}/{f}/"{x}"')
            print(f"SKIPPED {x}")
            continue

        os.system(f'ffmpeg -loglevel panic -i ./{dl_folder}/{f}/"{x}" ./{dl_folder}/{f}/"{artist} - {song}.mp3"')
        print(f"CONVERTED {x} -> {artist} - {song}.mp3")
        os.system(f'rm ./{dl_folder}/{f}/"{x}"')
        print(f"REMOVED {x}")

    print("\nOpen format.py to format metadata now!")