from fastapi import APIRouter
import json
import requests
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@router.get("/read")
def get_file():
    file = open("files/example.json", "r")
    content = json.load(file)
    file.close()
    return content

@router.get("/write")
def write_file():
    data = {"name": "John", "age": 30, "city": "New York"}
    file = open("files/example.json", "w")
    json.dump(data, file)
    file.close()
    return {"message": "File written successfully"}

@router.get("/external")
async def stream_file():
    try: 
        async def fetch_image():
            url = "https://fastly.picsum.photos/id/10/1900/800.jpg?hmac=hE4TBXQYwusXBV6_P4YfGnOaE1tErgtqJKJezI4aIm0"
            res = requests.get(url, stream=True)
            if res.status_code == 200:
                return res.content
            else:
                raise Exception("Failed to fetch image")
        # Call the async function to fetch the image
        content = await fetch_image()
        # Write the fetched image to a file
        with open("files/fetched_image.jpg", "wb") as img_file:
            img_file.write(content)
        return StreamingResponse(
            iter([content]),
            media_type="image/jpeg"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": e}

@router.get("/image")
def get_image():
    try:
        with open("files/fetched_image.jpg", "rb") as img_file:
            content = img_file.read()
        return StreamingResponse(
            iter([content]),
            media_type="image/jpeg"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": e}