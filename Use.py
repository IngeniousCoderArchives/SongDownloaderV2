import os
import youtube_dl
import ast
IS_WINDOWS = os.name == "nt"

input_menu = """ENTER THE NAME / URL OF THE SONG YOU WANT TO DOWNLOAD.
TO EXIT, TYPE "exit"."""


def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
while True:
    clear_screen()
    song_name = input(input_menu)
    if song_name == "exit":
      break
    else:
      file = open("Downloader.bat","w")
      pl = song_name
      file.write(f'youtube-dl -x --audio-format mp3 --no-playlist --default-search "ytsearch" "{pl}"')
      file.close()
      os.system("Downloader.bat")
      print("Downloaded")



