import time
import discord
import requests
import config

def getNgrokJson(link):
    return requests.get(link).json()["tunnels"]


def messageParser(tunnelName, tunnelUrl, msg):
    message = config.MESSAGE_TEMPLATE
    
    if msg != "" and message.find("%message%") != -1:
        message = message.replace("%message%", msg)
    elif msg == "" and message.find("%message%") != -1:
        message = message.replace("%message%", "no message") 

    if tunnelName != "" and message.find("%tunnel_name%") != -1:    
        message = message.replace("%tunnel_name%", tunnelName)
    if tunnelName != "" and message.find("%tunnel_url%") != -1:
        message = message.replace("%tunnel_url%", tunnelUrl)
    
    if tunnelUrl != "" and message.find("%host%") != -1:
        message = message.replace("%host%", tunnelUrl.split("//")[1].split(":")[0])
    if tunnelUrl != "" and message.find("%port%") != -1:
        message = message.replace("%port%", tunnelUrl.split("//")[1].split(":")[1])

    return message


def dictNgrokLinks():
    urlDict = {}
    for API_LINK in config.NGROK_LOCAL_API_LINKS:
        dataNgrokJson = getNgrokJson(API_LINK)
        for urlNgrokJson in dataNgrokJson:
            urlDict.update({urlNgrokJson["name"]: urlNgrokJson["public_url"]})

    return urlDict


def discordConnect():
    client = discord.Client(intents=discord.Intents.default())
    
    @client.event
    async def on_ready():
        ngrokLinks = dictNgrokLinks()
        for channel_id in config.DISCORD_CHANNEL_IDS_DATA:
            channel = client.get_channel(channel_id)
            print(f'\n{client.user} has connected to Discord!')
            print(f'sending links to {channel.name, channel.id, channel.guild.name}')

            print(f'deleting last {len(ngrokLinks.keys())} messages')
            if not config.TEST:
                await channel.purge(limit=len(ngrokLinks.keys()))

            for tunnelName in list(ngrokLinks.keys()):
                tunnelUrl = ngrokLinks[tunnelName]
                for keys in config.DISCORD_CHANNEL_IDS_DATA[channel_id].keys():
                    if tunnelName.find(keys) != -1 or keys == "all":
                        message = messageParser(tunnelName, tunnelUrl, config.DISCORD_CHANNEL_IDS_DATA[channel_id][keys])
                        print(message)
                        if not config.TEST:
                            await channel.send(message)
        print("\n\nBot Closed")
        await client.close()

    client.run(config.DISCORD_BOT_TOKEN)


def main():
    print("30 Seconds to start")
    time.sleep(30) # I added for this windows startup delay
    if config.TEST: print("\nTEST MODE ON\n")
    discordConnect()


if __name__ == "__main__":
    main()
