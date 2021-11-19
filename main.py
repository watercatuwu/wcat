from flask import Flask, render_template, request
from pytube import YouTube
import os
from moviepy.editor import *

#funtion
def ytdownload(url):
    #mp4
    yt = YouTube(url)

    print("Download video, please wait…")
    stream = yt.streams.get_lowest_resolution()
    stream.download(output_path=f"{os.environ['UserProfile']}/Desktop")
    print("Download completed")

    #mp3
    title = yt.title
    filename=f"{os.environ['UserProfile']}/Desktop/{title}.mp4"
    targetname=f"{os.environ['UserProfile']}/Desktop/{title}.mp3"
    video=VideoFileClip(filename)
    video.audio.write_audiofile(targetname)

#server(flask)
app = Flask(__name__, static_folder="./templates/assets")

@app.route('/')
def index():
    return render_template('yt.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.values.get('url')
    print(url)
    ytdownload(url)
    return F"url:{url}"

if __name__ == '__main__':
    app.run(port=8080)