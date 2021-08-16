from pytube import Playlist, YouTube
import os

p = Playlist(input("Enter playlist link:\n "))
f = input("Folder name (without / at the end):\n ./dl/")
print('\nNumber of videos in playlist: %s' % len(p.video_urls))

x = 1

for url in p.video_urls:
    yt = YouTube(url)
    t = yt.streams.filter(only_audio=True)
    t[0].download(f"dl/{f}/")

    print(f"FINISHED {x}: {url}")
    x = x+1

print("Done!")