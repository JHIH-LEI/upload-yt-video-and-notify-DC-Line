from notify_discord import notify_discord
from upload_video import upload_video
import asyncio

url = upload_video(yt_channel_id='UCYoAtenn8Tf6Aaz-CK8y-fw', new_video_file_path='video/test-for-upload.mp4')
asyncio.run(notify_discord(dc_channel_id=1065910741091233864, new_video_url=url))



