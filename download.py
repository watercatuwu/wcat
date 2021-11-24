from moviepy.editor import *
from pytube import YouTube

def mp4(url):
    yt = YouTube(url)

    print("Download video, please wait…")
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="/video")
    print("Download completed")

def mp3(url):
    yt = YouTube(url)
    title = yt.title
    print(F"Download {title}...")
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="./assets/video")
    file_size = round(stream.filesize/1048576, 2)
    print(F"{file_size}MB,done.")

    #mp3
    print(F"audio convert...")
    filename=f"./assets/video/{title}.mp4"
    targetname=f"./assets/video/{title}.mp3"
    video=VideoFileClip(filename)
    video.audio.write_audiofile(targetname)
    print("done.")
    return filename