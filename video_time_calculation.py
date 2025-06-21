import requests
from moviepy import VideoFileClip
from datetime import timedelta

def download_video(url: str, save_path: str = "downloaded_video.mp4") -> str:
    """
    Download a video from a given URL and save it to the specified path.

    Args:
        url (str): The URL of the video to download.
        save_path (str): The path where the downloaded video will be saved. Defaults to "downloaded_video.mp4".

    Returns:
        str: The path where the video is saved.

    Raises:
        Exception: If the video download fails, an exception is raised with details of the failure.
    """
    print("Downloading video...")
    try:
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Video downloaded successfully as '{save_path}'")
            return save_path
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to download video: {e}")

def get_video_duration(file_path: str) -> tuple[int, str]:
    """
    Calculate the duration of a video in seconds and return a formatted time string.

    Args:
        file_path (str): The path to the video file.

    Returns:
        tuple[int, str]: A tuple containing the duration in seconds and a formatted time string.

    Raises:
        Exception: If there is an error processing the video file, an exception is raised.
    """
    print("\n\nCalculating video duration...")
    try:
        with VideoFileClip(file_path) as clip:
            duration_seconds = int(clip.duration)
            formatted_duration = str(timedelta(seconds=duration_seconds))
        return duration_seconds, formatted_duration
    except Exception as e:
        raise Exception(f"Error processing video file: {e}")

if __name__ == "__main__":
    video_url = "https://codexspaces.sgp1.digitaloceanspaces.com/Codex/Math/1/1.%20Solids%20Around%20Us.mp4"
    video_save_path = "downloaded_video.mp4"

    try:
        video_path = download_video(video_url, video_save_path)
        seconds, formatted = get_video_duration(video_path)
        print(f"Video Duration: {seconds} seconds ({formatted})")

    except Exception as e:
        print(f"An error occurred: {e}")
