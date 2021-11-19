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

    print("Download video, please wait…")
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="/video")
    print("Download completed")

    #mp3
    title = yt.title
    filename=f"{os.environ['UserProfile']}/Desktop/{title}.mp4"
    targetname=f"{os.environ['UserProfile']}/Desktop/{title}.mp3"
    video=VideoFileClip(filename)
    video.audio.write_audiofile(targetname)

def info(url):
    yt = YouTube(url)
    author = yt.author
    title = yt.title
    return author, title