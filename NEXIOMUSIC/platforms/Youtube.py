import os
import re
import asyncio
import yt_dlp
from typing import Union
from youtubesearchpython.__future__ import VideosSearch
from YouTubeMusic.Search import Search as YTMusicSearch


class YouTubeAPI:
    def __init__(self, download_dir="downloads"):
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)
        self.base = "https://www.youtube.com/watch?v="
        self.listbase = "https://youtube.com/playlist?list="

    # ---------------------------
    # YouTube Normal Search
    # ---------------------------
    async def search(self, query: str, limit: int = 5):
        results = VideosSearch(query, limit=limit)
        return (await results.next()).get("result", [])

    async def details(self, link: str):
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return {
                "title": result["title"],
                "duration": result["duration"],
                "video_id": result["id"],
                "thumbnail": result["thumbnails"][0]["url"].split("?")[0],
                "url": f"https://www.youtube.com/watch?v={result['id']}"
            }

    # ---------------------------
    # YouTube Music Search
    # ---------------------------
    async def music_search(self, query: str, limit: int = 1):
        results = await YTMusicSearch(query, limit=limit)
        if not results or not results.get("main_results"):
            return None
        item = results["main_results"][0]
        return {
            "title": item.get("title"),
            "artist": item.get("artist_name"),
            "channel": item.get("channel_name"),
            "duration": item.get("duration"),
            "views": item.get("views"),
            "thumbnail": item.get("thumbnail"),
            "url": item.get("url"),
        }

    # ---------------------------
    # Download
    # ---------------------------
    async def download_audio(self, link: str):
        """Download audio (mp3)"""
        def _dl():
            opts = {
                "format": "bestaudio/best",
                "outtmpl": f"{self.download_dir}/%(id)s.%(ext)s",
                "quiet": True,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(link, download=True)
                filename = ydl.prepare_filename(info)
                return os.path.splitext(filename)[0] + ".mp3"
        return await asyncio.get_event_loop().run_in_executor(None, _dl)

    async def download_video(self, link: str):
        """Download video (720p max)"""
        def _dl():
            opts = {
                "format": "bestvideo[height<=720]+bestaudio/best",
                "merge_output_format": "mp4",
                "outtmpl": f"{self.download_dir}/%(id)s.%(ext)s",
                "quiet": True,
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(link, download=True)
                filename = ydl.prepare_filename(info)
                if not filename.endswith(".mp4"):
                    filename = os.path.splitext(filename)[0] + ".mp4"
                return filename
        return await asyncio.get_event_loop().run_in_executor(None, _dl)

    # ---------------------------
    # Playlist Extract
    # ---------------------------
    async def playlist(self, playlist_url: str, limit: int = 50):
        """Fetch video IDs from a playlist"""
        cmd = [
            "yt-dlp",
            "-i", "--get-id",
            "--flat-playlist",
            "--playlist-end", str(limit),
            "--skip-download",
            playlist_url
        ]
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise Exception(f"Error: {stderr.decode()}")
        return [vid for vid in stdout.decode().split("\n") if vid.strip()]


# ---------------------------
# Example usage
# ---------------------------
async def main():
    yt = YouTubeAPI()

    # YouTube Music Search
    print("🎵 Music Search...")
    music = await yt.music_search("Arijit Singh Tum Hi Ho", limit=1)
    print(music)

    # Normal YouTube Search
    print("🔎 YouTube Search...")
    results = await yt.search("Alan Walker Faded", limit=1)
    print(results[0])

    url = results[0]["link"]

    # Download Audio
    print("📥 Downloading audio...")
    audio_path = await yt.download_audio(url)
    print("Audio saved at:", audio_path)


if __name__ == "__main__":
    asyncio.run(main())
