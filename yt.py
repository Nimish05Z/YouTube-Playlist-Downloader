from pytube import Playlist
from pytube import YouTube
from pytube import Channel

# Replace 'PLAYLIST_URL' with the URL of the YouTube playlist you want to download
PLAYLIST_URL = 'https://www.youtube.com/watch?v=7Dh73z3icd8&list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR&pp=iAQB'

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    
    for video_url in playlist.video_urls:
        try:
            youtube_video = YouTube(video_url)
            video_stream = youtube_video.streams.get_highest_resolution()  # You can customize the stream you want
            print(f"Downloading: {youtube_video.title}")
            video_stream.download(output_path="downloaded_videos/")  # Change the output path as needed
            print(f"{youtube_video.title} downloaded successfully!\n")
        except Exception as e:
            print(f"Error downloading {video_url}: {e}\n")

if __name__ == "__main__":
    download_playlist(PLAYLIST_URL)
