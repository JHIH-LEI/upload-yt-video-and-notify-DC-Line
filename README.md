# upload-yt-video-and-notify-dc
Upload video to youtube and then notify discord channel.

# Demo
執行main.py的結果：
![](https://i.imgur.com/s206GSy.png)
![](https://i.imgur.com/BGsPLJP.png)
![](https://i.imgur.com/B3Hpm0x.png)

# How To Use?

我們需要5樣東西，有四樣會作為function的參數傳入，token則放在dotenv檔：
* OAuth憑證
* 要上傳的影片（我們需要它的路徑）
* Youtube頻道id
* Discord頻道id
* Discord機器人token

請注意：

如果要使用該服務，需要使用到Google Cloud Console的Youtube Data API，每推播一次影片會消耗1600扣打。免費帳戶每天只有9600，代表一天只能上傳6支影片。

接下來會教大家怎麼拿到需要的東西來開始專案已知如何做，只需要去main.py替換呼叫function的參數就好：
```=python
url = upload_video(yt_channel_id='放你youtube頻道id', new_video_file_path='放你影片檔案位置',
                   secret_file_path='放你憑證密鑰檔案位置')
asyncio.run(notify_discord(dc_channel_id=放你dc頻道id, new_video_url=url))
```
並且把.env.example改成.env檔，並且放上你的discord bot token。

# OAuth憑證
首先，你需要在Google Cloud Console創建一個專案，並且啟用YouTube Data API v3服務
![](https://i.imgur.com/lZj5nX2.png)

再來，你還需要使用OAuth2.0來驗證（因為不支援service account憑證來打api會得到401 ）
![](https://i.imgur.com/JNnBXQY.jpg)
參考資料：https://developers.google.com/youtube/v3/docs/errors
為了使用OAuth驗證，你需要先創建：

* OAuth同意畫面
* OAuth2.0憑證

![](https://i.imgur.com/P7TDIJf.png)

OAuth同意畫面跟著流程設定就好，要注意的是做完之後要**新增測試使用者**，測試使用者放上你要發布到youtube頻道的頻道擁有者email

![](https://i.imgur.com/tZolHsF.jpg)

接著到憑證，點擊建立憑證->OAuth用戶端ID

![](https://i.imgur.com/sJ1tIU6.png)

要開啟上傳youtube的權限 /auth/youtube.upload

建好之後下載json檔，放進專案同層資料夾中，並命名為client_secret.json，或是修改參數：

```=python
upload_video(..., secret_file_path="填上你的json檔案路徑")
```

# Youtube頻道id

![](https://i.imgur.com/5D4WmHc.png)

或著你可以到這邊找到：

![](https://i.imgur.com/gDzGixn.png)

![](https://i.imgur.com/6VRHlYx.png)

# Discord頻道id
到伺服器選擇想要推送的頻道，對其按右鍵，複製頻道id。
![](https://i.imgur.com/rUcs9XQ.png)

# Discord機器人token
[教學影片](https://youtu.be/2duDpbVsCwA)

到這個網址新增app，再新增bot，
https://discord.com/developers/applications

首先，創建一個app, 再來創建bot,點擊Reset Token可以拿到Token：

![](https://i.imgur.com/zKZYiql.png)

我們把這個token放到.env檔中的DISCORD_BOT_TOKEN

再來把機器人邀請到你的頻道：
![](https://i.imgur.com/DL9zs3N.png)

往下滑一點，有一個網址可以複製，進去這個網址，就能把機器人加到你指定的伺服器了：

![](https://i.imgur.com/rbvjscb.png)

![](https://i.imgur.com/JDhY99F.png)



### Now You Get Everything You Need!
* OAuth json檔
* 要上傳的影片的檔案路徑
* 要上傳到的Youtube頻道id
* Discord頻道id
* Discord機器人token （放在env檔）


Let's run program!

打開main.py這隻檔案並且替換這四個參數值：
* yt_channel_id
* new_video_file_path
* secret_file_path
* dc_channel_id

```=python
url = upload_video(yt_channel_id='放你youtube頻道id', new_video_file_path='放你影片檔案位置',
                   secret_file_path='放你憑證密鑰檔案位置')
asyncio.run(notify_discord(dc_channel_id=放你dc頻道id, new_video_url=url))
```

記得檢查.env檔的token有放上dc bot的token喔～

接著，打開終端機，執行main.py這隻檔案，


運行後會跳出一個授權頁面要你授權，請注意：

**這邊登入的用戶必須等於你剛剛加入到google oauth測試帳號的帳戶也必須等於youtube頻道所有者的帳戶！**

![](https://i.imgur.com/8xfECDZ.png)

授權後關閉網頁，接下來就等魔法發生吧～

成功後會看到以下畫面：

![](https://i.imgur.com/s206GSy.png)
