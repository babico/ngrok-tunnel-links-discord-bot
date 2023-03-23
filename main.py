import discord
import requests
import time

DISCORD_BOT_TOKEN = "<enter dicord token>"
DISCORD_CHANNEL_IDS = [749512222739736577, 761123456787039272, 1051234234507268648]
NGROK_LOCAL_API_LINKS = ["http://localhost:4040/api/tunnels/", "http://localhost:4041/api/tunnels/"]


def getNgrokJson(link):
    return requests.get(link).json()["tunnels"]


def dictNgrokLinks():
    urlDict = {}
    for API_LINK in NGROK_LOCAL_API_LINKS:
        dataNgrokJson = getNgrokJson(API_LINK)
        for urlNgrokJson in dataNgrokJson:
            urlDict.update({urlNgrokJson["name"]: urlNgrokJson["public_url"]})

    return urlDict


def discordConnect():
    client = discord.Client(intents=discord.Intents.default())


    @client.event
    async def on_ready():
        ngrokLinks = dictNgrokLinks()
        for channel_id in DISCORD_CHANNEL_IDS:
            channel = client.get_channel(channel_id)
            print(f'\n{client.user} has connected to Discord!')
            print(f'sending links to {channel.name}')
            
            print(f'deleting last {len(ngrokLinks.keys())} messages')
            await channel.purge(limit=len(ngrokLinks.keys()))

            for tunnelName in list(ngrokLinks.keys()):
                tunnelUrl = ngrokLinks[tunnelName]
                print(f"{tunnelName}, {tunnelUrl}")
                await channel.send(f"{tunnelName}, {tunnelUrl}")

        print("\n\nBot Closed")
        await client.close()
        
    client.run(DISCORD_BOT_TOKEN)


def ngrokTest():
    ngrokLinks = dictNgrokLinks()
    for channel_id in DISCORD_CHANNEL_IDS:
        print('\nBot has connected to Discord!')
        print(f'sending links to {channel_id}')

        print(f'deleting last {len(ngrokLinks.keys())} messages')
        for tunnelName in list(ngrokLinks.keys()):
            tunnelUrl = ngrokLinks[tunnelName]
            print(f"{tunnelName}, {tunnelUrl}")
            

    print("Bot Closed")


def main():
    print("30 Seconds to start")
    time.sleep(30) # I added for this windows startup delay
    discordConnect()
    # ngrokTest()


if __name__ == "__main__":
    main()
