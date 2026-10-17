import re
from urllib.parse import urlparse, parse_qs

from fastapi import FastAPI, HTTPException, Query
from youtube_transcript_api import YouTubeTranscriptApi
app = FastAPI(title="YouQube")

transcript_api = YouTubeTranscriptApi()

@app.get("/")
def home():
    return{
        "message":"YouQube backend is running!"
    }

def extract_video_id(url: str)->str:
    """Extract a YoutTube video ID from a supported URL."""
    parsed = urlparse(url)
    host = parsed.netloc.lower().split(":")[0]