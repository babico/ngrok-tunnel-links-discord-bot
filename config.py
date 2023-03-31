TEST = False

DISCORD_BOT_TOKEN = "<enter dicord token>"

NGROK_LOCAL_API_LINKS = [
    "http://257.21.68.4:4040/api/tunnels/",
    "http://172.56.77.289:4040/api/tunnels/",
    "http://268.1.55.58:4040/api/tunnels/"
]

# %tunnel_name% %tunnel_url% %message% %ngrok_host% %ngrok_port% 
# are placeholders for message
# 
# EXAMPLES:
# %tunnel_name%: homeserver-ssh 
# %tunnel_url%:  tcp://2.tcp.eu.ngrok.io:10480
# %message%:     usage:\n\t\t\t`ssh <username>@%ngrok_host% -p %ngrok_port%`
# %ngrok_host%:  2.tcp.eu.ngrok.io
# %ngrok_port%:  10480
MESSAGE_TEMPLATE = """
tunnel name: %tunnel_name%
    tunnel url: %tunnel_url%
    tunnel message: %message%
"""

# all: send all tunnels to this channel
# 
# message template placeholders are also supported for specified
# tunnel messages of each channel
DISCORD_CHANNEL_IDS_DATA = {
    749593882739736577: {
        "all": "", # no massage
    },
    1050897563907268648: {
        "babico": "",  # no massage
        "homeserver": "" # no massage
    },
    1085885700924256306: {
        "homeserver-ssh": "usage:\n\t\t\t`ssh <username>@%ngrok_host% -p %ngrok_port%`"
    },
}