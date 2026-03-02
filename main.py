from fastapi import FastAPI
import yt_dlp
import uuid

app = FastAPI()

@app.post("/download")
async def download_video(url: str):

    filename = f"videos/{uuid.uuid4()}.mp4"

    ydl_opts = {
        "outtmpl": filename,
        "format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return {
        "status": "success",
        "file": filename
    }