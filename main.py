from flask import Flask, render_template, request
from pytube import YouTube
import os
import schedule
import download as dl

#schedule
def delfile():
    path  = 'assets/video'
    files_in_dir = os.listdir(path)

    for file in files_in_dir:
        os.remove(f'{path}/{file}')
    os.rmdir(path) 
schedule.every().day.at('00:00').do(delfile)

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

@app.route('/dashboard')
def dashboard():
    file_size = 0
    path = 'assets/video'
    try:
        for fileName in os.listdir(path):
            file_size += os.path.getsize(path+'/'+fileName)
        file_size = round(file_size/1048576, 2)
        print(file_size, "mb")
    except:
        file_size = 0
    return render_template('dashboard.html',file_size=file_size)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)