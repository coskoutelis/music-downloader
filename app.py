from flask import Flask, render_template, request, Response
from pytubefix import YouTube, Search
import os
import time

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


def download_song(song_url):
    try:
        yt = YouTube(song_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        download_path = audio_stream.download(output_path=DOWNLOAD_FOLDER)
        return f"Downloaded: {os.path.basename(download_path)}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_youtube_url(song_title):
    try:
        search_results = Search(song_title).videos
        if search_results:
            return search_results[0].watch_url
        else:
            return None
    except Exception as e:
        return None


def remove_timestamps(text):
    lines = text.strip().split("\n")
    return [line.split(" ", 1)[-1] for line in lines if " " in line]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/progress')
def progress():
    songs_str = request.args.get('songs_str', '')
    song_titles = remove_timestamps(songs_str)

    def generate():
        for song_title in song_titles:
            youtube_url = get_youtube_url(song_title)
            if youtube_url:
                yield f"data: Found URL for '{song_title}': {youtube_url}\n\n"
                download_result = download_song(youtube_url)
                yield f"data: {download_result}\n\n"
            else:
                yield f"data: No URL found for '{song_title}'\n\n"
            time.sleep(1)  # Simulate delay for testing
        yield "data: All downloads completed\n\n"

    return Response(generate(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True)
