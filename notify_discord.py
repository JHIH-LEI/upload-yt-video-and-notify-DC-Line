import discord

from dotenv import load_dotenv
from os import getenv


async def notify_discord(dc_channel_id, new_video_url):
    load_dotenv()
    token = getenv('DISCORD_BOT_TOKEN')

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    # 利用decorator註冊一個on_ready事件的處理func
    @client.event
    async def on_ready():
        print(f'discord已經連線. Logged as {client.user}')
        discord_channel = client.get_channel(int(dc_channel_id))
        print(f'推播新影片消息至 {discord_channel} 頻道')
        await discord_channel.send('New Video Arrive! Check it out: ' + new_video_url)
        await client.close()

    # 連線到dc伺服器
    await client.start(token)




