from flask import Flask, render_template, request
from pytube import YouTube
import os
import download


#server(flask)
app = Flask(__name__, static_folder="./templates/assets")

@app.route('/')
def index():
    return render_template('yt.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.values.get('url')
    yt= YouTube(url)
    return render_template('yt_result.html',author=yt.author,title=yt.title,thumbnail=yt.thumbnail_url)

if __name__ == '__main__':
    app.run(port=8080,debug=True)