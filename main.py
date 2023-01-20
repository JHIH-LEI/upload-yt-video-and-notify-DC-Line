from notify_discord import notify_discord
from upload_video import upload_video
from notify_line import notify_to_line
import asyncio

url = upload_video(yt_channel_id='UCYoAtenn8Tf6Aaz-CK8y-fw', new_video_file_path='video/test-for-upload.mp4',
                   secret_file_path='client_secret.json')
asyncio.run(notify_discord(dc_channel_id=1065910741091233864, new_video_url=url))
notify_to_line(f'New Video Arrive! {url}')


