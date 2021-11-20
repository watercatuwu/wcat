from flask import Flask, render_template, request
from pytube import YouTube
import os
import download as dl


#server(flask)
app = Flask(__name__, static_folder="./assets")

@app.route('/')
def index():
    return render_template('yt.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.values.get('url')
    yt= YouTube(url)
    dl.mp3(url)
    return render_template('yt_result.html',author=yt.author,title=yt.title,thumbnail=yt.thumbnail_url,mp3=F"video/{yt.title}.mp3",mp4=F"video/{yt.title}.mp4")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)