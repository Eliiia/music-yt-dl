# music-yt-dl

If this code is formatted weirdly or just otherwise doesn't use normal python standards, I usually code in node, so i apologise.

Iffff you want to use this, feel free, I guess. I didn't put a licence because I wasn't sure what to put. I would appreciate it if you asked me somehow before forking this into a seperate thing, but I mean, it's your choice and i'll likely never even notice or care.

### Usage
Normal person usage goes something like:
1. Enter playlist link (something not private)
2. Enter folder inside ./dl/ that you want to contain the files (e.g. ./dl/cavetown)
3. Wait for each video to be downloaded inside ./dl/folder_name
4. If you want the audio-only mp4 videos to be downloaded and you have ffmpeg, say yes to the prompt
5. Give the artist name (e.g. cavetown)
6. The filename will be displayed. Using the file name, determine the name of the song and input it, OR write "SKIP"/"skip" to skip past this file.
7. Repeat step 6 until done.
8. Inside ./dl/folder_name, you will find your mp3 files

### Helping or something??
if you use this program for some reason and you want to contribute, idk, just do a pull request and i will probably notice it at some point

### Prerequisites
- Python.. obviously 
- youtube_dl: `pip install pytube`
- ffmpeg, if you wish to convert audio-only .mp4 files to .mp3 files automatically and do all the other stuff (it will ask you)

### To-do for the future, since I have nowhere else to put it
(that I'd remember)
[ ] Make it edit metadata after converting to mp3
[ ] Make a search feature thing instead of only using playlist links for the download