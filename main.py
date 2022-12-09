import discord
import requests
import time

DISCORD_BOT_TOKEN = "<enter dicord token>"
DISCORD_CHANNEL_IDS = [749512342739736577, 761123457187039272, 1050891234507268648]
NGROK_LOCAL_API_LINK = "http://localhost:4040/api/tunnels/"


def getNgrokJson(link):
    return requests.get(link).json()["tunnels"]


def dictNgrokLinks():
    dataNgrokJson = getNgrokJson(NGROK_LOCAL_API_LINK)
    urlDict = {}

    for urlNgrokJson in dataNgrokJson:
        urlDict.update({urlNgrokJson["name"]: urlNgrokJson["public_url"]})

    return urlDict


def discordConnect():
    client = discord.Client(intents=discord.Intents.default())


    @client.event
    async def on_ready():
        for channel_id in DISCORD_CHANNEL_IDS:
            channel = client.get_channel(channel_id)
            print(f'{client.user} has connected to Discord!')
            print(f'sending links to {channel.name}')

            print(f'deleting last 3 messages')
            await channel.purge(limit=3)
            for tunnelName in list(dictNgrokLinks().keys()):
                tunnelUrl = dictNgrokLinks()[tunnelName]
                print(f"{tunnelName}, {tunnelUrl}")
                await channel.send(f"{tunnelName}, {tunnelUrl}")

        print("Bot Closed")
        await client.close()
        
    client.run(DISCORD_BOT_TOKEN)


def main():
    time.sleep(30) # I added for this windows startup delay
    discordConnect()


if __name__ == "__main__":
    main()
