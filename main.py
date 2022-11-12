import discord
import requests

DISCORD_BOT_TOKEN = "<enter dicord token>"
DISCORD_CHANNEL_ID = <enter channel id>
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
        print(f'{client.user} has connected to Discord!')
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        
        for tunnelName in list(dictNgrokLinks().keys()):
            tunnelUrl = dictNgrokLinks()[tunnelName]
            print(f"{tunnelName}, {tunnelUrl}")
            await channel.send(f"{tunnelName}, {tunnelUrl}")
        print("Bot Closed")
        await client.close()
        
    client.run(DISCORD_BOT_TOKEN)

def main():
    discordConnect()

if __name__ == "__main__":
    main()
    
