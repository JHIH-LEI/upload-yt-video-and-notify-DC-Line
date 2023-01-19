from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError

# 進度條
from tqdm import tqdm

# os
from os.path import getsize

# 官方範例提供的auth方式做修改
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPE = ['https://www.googleapis.com/auth/youtube.upload']


# Oauth2
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret_33.json', scopes=SCOPE)
    creds = flow.run_local_server()
    return build('youtube', 'v3', credentials=creds)


# create youtube api client
youtube = get_authenticated_service()

# replace your channel_id
channel_id = 'UCYoAtenn8Tf6Aaz-CK8y-fw'
# plz update file path to upload
new_video_file_path = "video/test-for-upload.mp4"
video_file = open(new_video_file_path, 'rb')
video_size = getsize(new_video_file_path)

chunk_size_of_25per = video_size * 0.25
# 每25 %會通知,進度監控管理，影片快上傳完通知？

media = MediaIoBaseUpload(video_file, mimetype='video/mp4', resumable=True, chunksize=1024*1024)


def upload_video():
    try:
        # upload video
        # 注意，上傳影片會消耗quota 1600單位，免費帳號上限為9600，代表一天六次
        video_upload_request = youtube.videos().insert(
            part="snippet,status",
            body={
                'snippet': {
                    'title': '測試',
                    'description': '測試看看',
                    'tags': [],
                    'categoryId': '',
                    'channelId': channel_id
                },
                'status': {
                    'privacyStatus': 'public'
                }
            },
            # 檔案大的情況下，可以用MediaIoBaseUpload接受二進位流作為參數，搭配file對象、StringIO對象來實現，比較快上傳，因為不需要將整個檔案讀取到內存。
            media_body=media
        )

        # TODO: 進度條管理＋request
        # with tqdm(total=media.size()) as pbar:
        #     while video_upload_request.next_chunk():
        #         pbar.update(video_upload_request.next_chunk())

        response = video_upload_request.execute()
        # TODO: 自動打開影片？
        print(f'影片上傳成功： https://www.youtube.com/watch?v={response["id"]}')
        print(response)
        # TODO: 成功上傳後，發discord推播通知

    except HttpError as e:
        print(f'An Error Occurred When Upload Video to Youtube: {e}')


upload_video()