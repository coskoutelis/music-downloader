from flask import Flask, render_template, request, redirect, url_for
import yt_dlp

app = Flask(__name__)

# Function to download song from YouTube
def download_song(song_title):
    ydl_opts = {
        'format': 'bestaudio/best',  # Select best audio quality
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': './downloads/%(title)s.%(ext)s',  # Output directory for downloaded song
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Search and download the song
        search_query = f"ytsearch:{song_title}"
        ydl.download([search_query])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        song_title = request.form['song_title']
        download_song(song_title)  # Call the download function
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
